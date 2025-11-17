"""
Harness to run many XML inputs safely:
 - runs process_request.py in a subprocess (optionally allowing XXE)
 - captures stdout, stderr, exitcode
 - reads app/runtime.log to detect file reads and warnings
 - runs static_checks to label inputs and merges dynamic evidence
Outputs a JSON summary at the end.
"""
import sys, json, subprocess
from pathlib import Path
from collections import defaultdict
from lxml import etree
import re

from bug_specs import BUG_SPECS_XML
from xml_concretizer.auth_service_xml.utils import wrap_with_doctype
from xml_concretizer.utils import gen_sensitive_paths
try:    
    from .static_checker import static_checks
except ImportError:
    from xml_concretizer.auth_service_xml.fuzzing.static_checker import static_checks

BASE = Path(__file__).parent.parent
APP = BASE / "app" / "process_request.py"
LOG = BASE / "app" / "runtime.log"

SENS = gen_sensitive_paths()
PROJECT_LOCAL_SET = SENS["project_local"]
SYSTEM_SET = SENS["system"]

SENSITIVE_READ_PAT = re.compile(r"(?:/etc/|/proc/|/dev/|file:///|/root/|\\.env|session_tokens|server\.key)", re.IGNORECASE)
SCHEMA_PATHS = [BASE /"config" / "message.xsd",BASE /"config" / "file.xsd",BASE /"config" / "query.xsd",BASE /"config" / "request.xsd",BASE /"config" / "user.xsd" ]
def classify_read_path(p: str):
    # normalize
    p = p.strip()
    # exact membership checks first
    if p in SYSTEM_SET:
        return "system_file_read"
    if p in PROJECT_LOCAL_SET or "/auth_service_xml/" in p or p.startswith(str(Path.cwd())):
        return "local_repo_file_read"
    # regex fallbacks
    if SENSITIVE_READ_PAT.search(p):
        return "system_file_read_sensitive_read_pat"
    # check for relative traversal
    if "../" in p:
        return "system_file_read_relative"
    return None

def run_single(input_path: str, allow_xxe=False, timeout=5):
    abs_input = str(Path(input_path).resolve())
    cmd = [sys.executable, "-m","app.process_request", abs_input]
    if allow_xxe:
        cmd.append("--allow-xxe")
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=str(BASE))
        stdout = proc.stdout
        stderr = proc.stderr
        rc = proc.returncode
    except subprocess.TimeoutExpired:
        return {"timeout": True}
    # read runtime log for file-access lines
    log_lines = []
    if LOG.exists():
        try:
            with open(LOG, "r", encoding="utf-8") as f:
                log_lines = f.readlines()
        except Exception:
            log_lines = []
    # run static checks
    with open(input_path, "r", encoding="utf-8") as f:
        xml_text = f.read()
    static_labels = static_checks(xml_text)
    # heuristics: if runtime.log contains "read_file path=", mark dynamic file read
    # dynamic classification
    dyn = set()
    # collect the exact paths read (optional)
    read_paths = []
    for line in log_lines[-200:]:
        # try structured pattern first
        m = re.search(r"read_file path=([^\s]+)", line)
        if m:
            p = m.group(1).strip()
            read_paths.append(p)
            cls = classify_read_path(p)
            if cls:
                dyn.add(cls)
       
        # Detect XPath execution
        m = re.search(r"XPath executed; selector=(.+?); matches=(\d+)", line)
        if m:
            selector = m.group(1).strip()
            matches = int(m.group(2))
            dyn.add("xpath_query_executed")

        # Detect XPath error
        if "XPath error for selector=" in line:
            dyn.add("BUG06_xpath_injection_error")
        
        if "numeric parse error" in line:
            dyn.add("numeric_parsing_error")
        

    # final triggered bugs: only dynamic-confirmed ones (but keep static candidates in result)
    final_triggered = set()
    if "system_file_read" in dyn:
        final_triggered.add("system_file_read")
    if "local_repo_file_read" in dyn:
        final_triggered.add("local_repo_file_read")
    if "system_file_read_sensitive_read_pat" in dyn:
        final_triggered.add("system_file_read_sensitive_read_pat")
    if "system_file_read_relative" in dyn:
        final_triggered.add("system_file_read_relative")
    
    result = {
        "stdout": stdout,
        "stderr": stderr,
        "returncode": rc,
        "static_labels": list(static_labels),
        "dynamic_evidence": list(dyn),
        "log_tail": log_lines[-20:],
    }
    return result

def get_triggered_bugs(static_hits, dynamic_hits, bug_specs):
    """
    Determines which bugs are triggered given the lists of static and dynamic labels.

    Args:
        static_hits (list or set): Static triggers observed.
        dynamic_hits (list or set): Dynamic triggers observed.
        bug_specs (dict): The bug specification dictionary, with keys:
            - "static_triggers": list of static trigger labels
            - "dynamic_triggers": list of dynamic trigger labels

    Returns:
        list of dicts: Each dict contains:
            - 'bug_id': the bug key
            - 'description': bug description
            - 'motivation': bug motivation
            - 'matched_static': list of static triggers that matched
            - 'matched_dynamic': list of dynamic triggers that matched
    """
    triggered_bugs = []
    static_hits = set(static_hits)
    dynamic_hits = set(dynamic_hits)

    for bug_id, info in bug_specs.items():
        static_triggers = set(info.get("static_triggers", []))
        dynamic_triggers = set(info.get("dynamic_triggers", []))

        # Determine which triggers matched
        matched_static = list(static_triggers & static_hits)
        matched_dynamic = list(dynamic_triggers & dynamic_hits)

        # Conditions to trigger a bug:
        # - if static triggers exist, all of them must match
        # - if dynamic triggers exist, at least one must match
        static_ok = not static_triggers or matched_static == list(static_triggers)
        dynamic_ok = not dynamic_triggers or bool(matched_dynamic)

        if static_ok and dynamic_ok:
            triggered_bugs.append(bug_id)

    return triggered_bugs

def run_multi_bug_eval_xml_on_folder(folder, allow_xxe=False, bug_specs=BUG_SPECS_XML, harness_out_json="xml_concretizer/auth_service_xml/harness_results.json"):
    results = {}
    bug_counts = defaultdict(int)
    input_triggers = defaultdict(set)
    nb_bugs_total = len(bug_specs.keys())
    valid_count,invalid_count=0,0

    schemas = []
    for path in SCHEMA_PATHS:
        with open(path, "rb") as f:
            schema_root = etree.parse(str(path))
            schemas.append(etree.XMLSchema(schema_root))

    p = Path(folder)
    files = sorted([x for x in p.iterdir() if x.is_file() and x.suffix in ('.xml','.txt')])
    for f in files:
        # clear runtime.log before run
        try:
            open(LOG, "w").close()
        except Exception:
            pass

        with open(f, "r", encoding="utf-8") as file:
            input = file.read()
        
        def is_xml_valid(xml_string):
            """Return True if xml_string matches at least one schema."""
            for i,schema in enumerate(schemas):
                parser = etree.XMLParser(
                    schema=schema,
                    load_dtd=True,
                    resolve_entities=False, 
                    no_network=True,
                )
                # Inject a fake DOCTYPE declaration before the root element
                xml_with_doctype = xml_string
                if "<!DOCTYPE" not in xml_string:
                    xml_with_doctype = wrap_with_doctype(xml_string)
                try:
                    etree.fromstring(xml_with_doctype.encode("utf-8"), parser)
                    return True  # valid for this schema
                except etree.XMLSyntaxError as e:
                    continue
            return False
        
        is_valid = is_xml_valid(input)
        # if not is_valid:
        #     print(f"Invalid XML for input {f}")
            
        if is_valid:
            valid_count+=1
        else:
            invalid_count+=1
            continue

        res = run_single(str(f), allow_xxe=allow_xxe)
        results[str(f)] = res
        dynamic_hits = res.get("dynamic_evidence",[])
        static_hits = res.get("static_labels",[])
        triggered_bugs = get_triggered_bugs(static_hits, dynamic_hits, bug_specs)
        for bug in triggered_bugs:
            bug_counts[bug] += 1
            input_triggers[bug].add(input.strip())

    total_triggered = sum(bug_counts.values())
    nb_distinct_bugs_triggered = len(bug_counts)
    per_bug_counts_distinct = {bug: len(queries) for bug, queries in input_triggers.items()}
    total_distinct_queries = sum(per_bug_counts_distinct.values())
    avg_inputs_per_bug = round(total_triggered / nb_distinct_bugs_triggered, 2) if nb_distinct_bugs_triggered else 0
    avg_distinct_per_bug = round(total_distinct_queries / nb_distinct_bugs_triggered, 2) if nb_distinct_bugs_triggered else 0
    examples = {bug: list(queries) for bug, queries in input_triggers.items()}

    summary = {
        "executable_rate": round(valid_count / max(1, valid_count + invalid_count) * 100, 2),
        "nb_distinct_bugs_triggered": nb_distinct_bugs_triggered,
        "coverage": round(nb_distinct_bugs_triggered * 100 / max(1, nb_bugs_total), 2),
        "total_triggers": total_triggered,
        "total_distinct_queries": total_distinct_queries,
        "avg_inputs_per_bug": avg_inputs_per_bug,
        "avg_distinct_per_bug": avg_distinct_per_bug,
        "per_bug_counts": dict(bug_counts),
        "per_bug_counts_distinct": per_bug_counts_distinct,
        "per_bug_example": examples,
    }

    
    with open(harness_out_json, "w", encoding="utf-8") as fo:
        json.dump(results, fo, indent=2)
    print(f"Wrote results per file to {harness_out_json}")

    return summary

if __name__=="__main__":
    seeds = "xml_concretizer/auth_service_xml/seeds/"
    print(run_multi_bug_eval_xml_on_folder(seeds,True,"harness_test.json"))