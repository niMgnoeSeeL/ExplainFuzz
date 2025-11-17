import re
from collections import Counter
from lxml import etree
from pathlib import Path

from xml_concretizer.auth_service_xml.utils import wrap_with_doctype

SENSITIVE_PATTERNS = [
    r"\.\./",
    r"^/etc(/|$)",
    r"^/proc(/|$)",
    r"^/dev(/|$)",
    r"^file:///.+",
    r"^[A-Za-z]:\\",
]
_sens_re = re.compile("|".join(p for p in SENSITIVE_PATTERNS))

def is_numeric_overflow_candidate(a_val: str, bits=32) -> bool:
    """
    Returns True if the value could overflow a signed integer of 'bits' bits.
    """
    try:
        v = int(a_val)
        limit = 2**(bits-1) - 1  # max signed integer
        return abs(v) > limit
    except ValueError:
        return False


def static_checks(xml_text: str):
    labels = set()
    # 1) Doctype + Entity declarations (XXE candidate)
    if re.search(r'<!DOCTYPE[^>]+>', xml_text, re.IGNORECASE):
        if re.search(r'<!ENTITY\s+\w+\s+SYSTEM\s+["\']([^"\']+)["\']', xml_text, re.IGNORECASE):
            labels.add('xxe_candidate')
    xml_text = wrap_with_doctype(xml_text)
    
    suspicious_attr_names = {'src','href','path','file','xlink:href'}
    try:
        root = etree.fromstring(xml_text.encode('utf-8'))
    except Exception:
        return labels  # syntactically invalid; filter earlier

    map_num_nb_bits= {
        "quota": 64,
        "amount": 32,
        "repeat": 32,
        "limit": 32,
        "id": 64,
        "price": 32
        }
    for elem in root.iter():
        for attr_name, val in elem.attrib.items():
            name = attr_name.lower()
            if any(k in name for k in suspicious_attr_names):
                if "data/resources" in val or val.startswith(str(Path.cwd())):
                    labels.add('local_repo_path_candidate')
                elif _sens_re.search(val):
                    labels.add('path_traversal_candidate')
            if val and val.isdigit() and is_numeric_overflow_candidate(val, bits=map_num_nb_bits.get(name,32)):
                labels.add('numeric_overflow_candidate')

    ids = [elem.attrib.get('id') for elem in root.iter() if 'id' in elem.attrib]
    ids = [i for i in ids if i is not None]
    dup = [k for k,v in Counter(ids).items() if v>1]
    if dup:
        labels.add('duplicate_id_candidate')
    
    for elem in root.iter():
        for attr_name, val in elem.attrib.items():
            name = attr_name.lower()


    # Detect true XPath-like expressions and ignore file paths / URIs
    URI_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://")
    EXT_RE = re.compile(r"\.(txt|pdf|log|cfg|conf|json|xml|yaml|yml|pem|key|crt)$", re.IGNORECASE)

    # This pattern focuses only on real XPath syntax indicators
    # XPATH_LIKELY_RE = re.compile(
    #     r"(^//)|"                              # starts with //
    #     r"(/[\w-]+(\[[^\]]+\])?)|"             # has /step or /step[predicate]
    #     r"(\[[^\]]+\])|"                       # has predicate [ ... ]
    #     r"\b(self|descendant|ancestor|parent|child|text|node|contains|starts-with|concat|position)\b|"  # XPath axes/functions
    #     r"(\bor\b|\band\b|\=|\!=)",            # boolean or comparison operators
    #     re.IGNORECASE
    # )

    XPATH_RISKY_RE = re.compile(
    r"//|(\.\.)|\b(or|and)\b|"
    r"\[.*[=<>].*\]|"
    r"\b(self|descendant|ancestor|parent|child|text|node|contains|starts-with|concat|position)\b",
    re.IGNORECASE
)

    # Only 'select' and 'query' are relevant attributes for XPath
    XPATH_ATTRS = {"select", "query","xpath"}

    for elem in root.iter():
        for attr_name, val in elem.attrib.items():
            if not val:
                continue
            attr = attr_name.lower()

            # Control bug
            if attr=="q" and not val.startswith("/"):
                labels.add("incorrect_start_query")

            # only check typical XPath attributes
            if attr not in XPATH_ATTRS:
                continue

            # skip URIs or local file-like values
            if URI_SCHEME_RE.match(val) or EXT_RE.search(val):
                continue

            # flag true XPath-looking expressions
            if XPATH_RISKY_RE.search(val.strip()):
                labels.add("xpath_injection_candidate")
            

    for elem in root.iter():
        text = (elem.text or "").strip()
        if not text:
            continue

        # skip if text looks like a URI or filename
        if URI_SCHEME_RE.match(text) or EXT_RE.search(text):
            continue
        
        if not isinstance(elem.tag, str):
            continue  # skip comments, PIs, etc.

        # only check relevant tag names (same logic as for attributes)
        if elem.tag.lower() not in XPATH_ATTRS and elem.tag.lower() != "query":
            continue

        if XPATH_RISKY_RE.search(text):
            labels.add("xpath_injection_candidate")

    max_depth = 0
    def depth(elem, d=0):
        nonlocal max_depth
        max_depth = max(max_depth, d)
        for c in elem:
            depth(c, d+1)
    depth(root, 1)
    if max_depth > 30:
        labels.add('resource_exhaustion_candidate')

    ns_uris = set()
    for e in root.iter():
        for k,v in (e.nsmap or {}).items():
            if v: ns_uris.add(v)
    if len(ns_uris) > 3:
        labels.add('namespace_confusion_candidate')


    # 4) Comments bug
    comments = re.findall(r"<!--(.*?)-->", xml_text, flags=re.DOTALL)
    for c in comments:
        comment_content = c.strip()
        # approximate 'auth_bypass_detected' by looking for <user> or <role> inside comment
        if re.search(r"<\s*user\b|<\s*role\b", comment_content):
            labels.add("auth_bypass_detected")

    #5) Entity Ref
    unique_threshold = 5

    entity_pattern = re.compile(r"&([a-zA-Z0-9_]+);")

    matches = entity_pattern.findall(xml_text)
    entities = [e for e in matches if e not in {"lt", "gt", "amp", "apos", "quot"}]

    unique_entities = set(entities)

    is_suspicious_entity_ref = len(unique_entities) >= unique_threshold
    if is_suspicious_entity_ref:
        labels.add("entity_expansion_critic")


    # 6) CDATA 

    # Extract CDATA contents
    cdata_pattern = re.compile(r"<!\[CDATA\[(.*?)\]\]>", re.DOTALL)
    cdata_blocks = cdata_pattern.findall(xml_text)

    SENSITIVE_TAGS = {"user", "request", "query", "file", "note"}
    SENSITIVE_ATTRS = {"id", "username", "role", "file", "quota", "amount", "select", "path", "limit"}

    for block in cdata_blocks:
        block = block.strip()
        
        # Look for a sensitive tag with at least one sensitive attribute
        risky_tag_match = re.findall(r"<\s*(\w+)([^>]*)>", block)
        has_risky_tag = False
        for tag, attrs in risky_tag_match:
            if tag.lower() in SENSITIVE_TAGS:
                for attr_match in re.findall(r'(\w+)\s*=', attrs):
                    if attr_match.lower() in SENSITIVE_ATTRS:
                        has_risky_tag = True
                        break
            if has_risky_tag:
                break

        # Detect script or SQL
        has_script = bool(re.search(r"(script|onload|onclick|eval|alert|fetch)\s*\(", block, re.IGNORECASE))
        has_sql = bool(re.search(r"(SELECT|INSERT|UPDATE|DELETE)\s+", block, re.IGNORECASE))
        
        if has_risky_tag or has_script or has_sql:
            labels.add("cdata_injection_candidate")

    

    return labels
