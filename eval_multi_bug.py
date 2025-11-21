import json
import re
import os
from time import time
from bug_specs import BUG_SPECS_SQL, BUG_SPECS_XML
from custom_generator_sql.schema import retrieve_schema
from grammarinator_fuzzing.filter_inputs import (
    measure_multi_bug_rate,
    measure_multi_bug_rate_from_folder,
    read_queries_from_file
)
from main import RESULTS_DIR, get_literal_token_mapping, main_generate_inputs
from xml_concretizer.auth_service_xml.fuzzing.harness import run_multi_bug_eval_xml_on_folder


######### SHARED UTILITIES #########

def save_results_to_json(file_path, data):
    """Save evaluation results to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4, default=str)
    print(f"Results saved to {file_path}")


def load_results_from_json(file_path):
    """Load evaluation results from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


######### SQL DOMAIN EVALUATION #########

def eval_sql_multi_bug_rate(source, path, from_file=False, bug_specs=None, scenario=2, tok_condition=None):
    """
    Evaluate multi-bug rate for SQL inputs.

    Args:
        source: Name of the source (e.g., 'Grammarinator', 'ExplainFuzz', 'Seeds')
        path: Path to folder or file
        from_file: Whether to read from a single file or from a folder
        bug_specs: Bug specifications to use for evaluation
        scenario: Scenario number for evaluation
        tok_condition: Token condition for filtering
    """
    print(f"Evaluating {source}...")
    bug_specs = bug_specs or BUG_SPECS_SQL

    if from_file:
        print(f"Reading the file: {path}")
        queries = read_queries_from_file(path)
        return measure_multi_bug_rate(queries, bug_specs, scenario, tok_condition)
    else:
        return measure_multi_bug_rate_from_folder(path, bug_specs, scenario)


def eval_sql_grammarinator(domain, scenario, try_count=3):
    """Evaluate Grammarinator results for SQL domain."""
    results = []
    for try_id in range(1, try_count + 1):
        folder_path = f"data/intermediate/fuzz_outputs/{domain}/try-{try_id}/no-generate/"
        res = eval_sql_multi_bug_rate("Grammarinator", folder_path, from_file=False, scenario=scenario)
        results.append(res)
    return results


def eval_sql_explainfuzz(domain, scenario, tok_condition=None):
    """Evaluate ExplainFuzz results for SQL domain."""
    return eval_sql_multi_bug_rate(
        source="ExplainFuzz",
        path=f"data/output/inputs/{domain}/inputs_no_generate.txt",
        from_file=True,
        scenario=scenario,
        tok_condition=tok_condition
    )


def eval_sql_seeds(domain, scenario):
    """Evaluate seed inputs for SQL domain."""
    domain_seeds = domain[:-1] if domain[-1] in ["A", "B"] else domain
    return eval_sql_multi_bug_rate(
        source="Seeds",
        path=f"data/input/seeds/{domain_seeds}/",
        from_file=False,
        scenario=scenario
    )


def run_sql_multi_bug_evaluation(domain="SQL", mode="no-generate", num_inputs=10000, 
                                  repetitions=5, file_path=None, scenario=2):
    """
    Run complete multi-bug evaluation for SQL domain.
    
    Args:
        domain: SQL domain identifier
        mode: Generation mode
        num_inputs: Number of inputs to generate
        repetitions: Number of times to run ExplainFuzz evaluation
        file_path: Output file path (auto-generated if None)
        scenario: Scenario number for evaluation
    """
    results = {}
    
    # Evaluate seeds
    results["Seeds"] = eval_sql_seeds(domain, scenario)
    
    # Evaluate Grammarinator
    results["Grammarinator"] = eval_sql_grammarinator(domain, scenario)
    
    # Evaluate ExplainFuzz multiple times
    results["ExplainFuzz"] = []
    for _ in range(repetitions):
        main_generate_inputs(domain, mode, num_inputs, None)
        res = eval_sql_explainfuzz(domain, scenario)
        results["ExplainFuzz"].append(res)

    # Save results
    if not file_path:
        file_name = f"results_multi_bug_{domain}.json"
        folder_path = RESULTS_DIR / "bug_rate"
        file_path = folder_path / file_name

    save_results_to_json(file_path, results)
    print(f"🎉 SQL evaluation complete for {domain}")
    
    return results


def run_sql_conditioning_evaluation(domain, input_file_path, output_file_path, 
                                     num_inputs=10000, repetitions=3):
    """
    Run conditioning evaluation for SQL domain.
    
    Args:
        domain: SQL domain identifier
        input_file_path: Path to file with base results
        output_file_path: Path to save results with conditioning
        num_inputs: Number of inputs to generate
        repetitions: Number of repetitions per condition
    """
    all_results = load_results_from_json(input_file_path)
    literal_to_tokens = get_literal_token_mapping(domain)
    results_conditioning = []
    tokens_covered = set()
    
    # Retrieve database schema
    conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"
    schema = retrieve_schema(conninfo)

    # Evaluate each bug condition
    for _, bug_info in BUG_SPECS_SQL.items():
        required_tokens = bug_info["required"]
        lit_condition = required_tokens[0] if required_tokens else None
        tok_condition = literal_to_tokens.get(lit_condition, None)
        
        if tok_condition in tokens_covered:
            continue
       
        results_one_condition = []
        for _ in range(repetitions):
            print(f"Evaluating conditioning for token: {tok_condition}")
            main_generate_inputs(
                domain=domain,
                mode="no-generate",
                nb_concrete_inputs=num_inputs,
                token_condition=tok_condition,
                dry_run=True,
                schema=schema
            )
            res_conditioned = eval_sql_explainfuzz(domain, scenario=2, tok_condition=lit_condition)
            res_conditioned["conditioning_token"] = lit_condition
            results_one_condition.append(res_conditioned)
            tokens_covered.add(tok_condition)
        
        results_conditioning.append(results_one_condition)

    all_results["ExplainFuzz + conditioning"] = results_conditioning
    save_results_to_json(output_file_path, all_results)
    
    return all_results


######### XML DOMAIN EVALUATION #########

def clean_xml_text(xml_text):
    """
    Clean up XML generated by Grammarinator.
    
    Removes extraneous spaces and normalizes formatting while
    preserving spaces in text content and CDATA sections.
    """
    # Remove spaces immediately after '<' and before '>'
    xml_text = re.sub(r'<\s+', '<', xml_text)
    xml_text = re.sub(r'\s+>', '>', xml_text)
    
    # Remove spaces in closing tags
    xml_text = re.sub(r'</\s*([a-zA-Z_:][\w:.-]*)\s*>', r'</\1>', xml_text)

    # Remove spaces around '=' in attributes
    xml_text = re.sub(r'\s*=\s*', '=', xml_text)

    # Remove spaces before '/>' for self-closing tags
    xml_text = re.sub(r'\s+/>\s*', '/>', xml_text)

    # Remove spaces between adjacent tags
    xml_text = re.sub(r'>\s+<', '><', xml_text)

    # Strip leading/trailing whitespace on each line
    lines = [line.strip() for line in xml_text.splitlines() if line.strip()]

    return '\n'.join(lines)


def clean_xml_folder(folder_path):
    """Clean all XML files in a folder."""
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith((".txt", ".xml")):
                file_path = os.path.join(root, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    xml_text = f.read()
                
                cleaned_xml = clean_xml_text(xml_text)
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(cleaned_xml)


def eval_xml_grammarinator(domain, mode, repetitions=3):
    """Evaluate Grammarinator results for XML domain."""
    results = []
    for try_id in range(1, repetitions + 1):
        folder_path = f"data/intermediate/fuzz_outputs/{domain}/try-{try_id}/{mode}/"
        clean_xml_folder(folder_path)
        res = run_multi_bug_eval_xml_on_folder(folder_path, allow_xxe=True)
        results.append(res)
    return results


def eval_xml_explainfuzz(domain, mode, num_inputs=10000, repetitions=3):
    """Evaluate ExplainFuzz results for XML domain."""
    results = []
    folder_path = f"data/output/inputs/{domain}/test_inputs_{mode.replace('-', '_')}"
    
    for _ in range(repetitions):
        start = time()
        main_generate_inputs(domain, mode, num_inputs, None)
        print("Running multi-bug evaluation...")
        res = run_multi_bug_eval_xml_on_folder(folder_path, allow_xxe=True)
        results.append(res)
        elapsed = time() - start
        print(f"Evaluation took {elapsed:.1f}s")
    
    return results


def eval_xml_seeds(domain):
    """Evaluate seed inputs for XML domain."""
    domain_seeds = domain[:-1] if domain[-1] in ["A", "B"] else domain
    folder_path = f"data/input/seeds/{domain_seeds}/"
    return run_multi_bug_eval_xml_on_folder(folder_path, allow_xxe=True)


def run_xml_multi_bug_evaluation(domain, output_file, num_inputs=10000, 
                                  mode="no-generate", repetitions=3):
    """
    Run complete multi-bug evaluation for XML domain.
    
    Args:
        domain: XML domain identifier
        output_file: Path to save results
        num_inputs: Number of inputs to generate
        mode: Generation mode
        repetitions: Number of repetitions for Grammarinator and ExplainFuzz
    """
    all_results = load_results_from_json(output_file)
    
    print("Evaluating seeds...")
    all_results["Seeds"] = eval_xml_seeds(domain)
    save_results_to_json(output_file, all_results)

    print("Evaluating Grammarinator...")
    all_results["Grammarinator"] = eval_xml_grammarinator(domain, mode, repetitions)
    save_results_to_json(output_file, all_results)

    print("Evaluating ExplainFuzz...")
    all_results["ExplainFuzz"] = eval_xml_explainfuzz(domain, mode, num_inputs, repetitions)
    save_results_to_json(output_file, all_results)

    print(f"🎉 XML evaluation complete for {domain}")
    return all_results


def run_xml_conditioning_evaluation(domain, input_file_path, output_file_path, 
                                     num_inputs=10000, repetitions=3, mode="no-generate"):
    """
    Run conditioning evaluation for XML domain.
    
    Args:
        domain: XML domain identifier
        input_file_path: Path to file with base results
        output_file_path: Path to save results with conditioning
        num_inputs: Number of inputs to generate
        repetitions: Number of repetitions per condition
        mode: Generation mode
    """
    all_results = load_results_from_json(input_file_path)
    results_conditioning = []
    tokens_covered = set()
    folder_path = f"data/output/inputs/{domain}/test_inputs_{mode.replace('-', '_')}"

    # Evaluate each bug condition
    for _, bug_info in BUG_SPECS_XML.items():
        tok_condition = bug_info.get("cond_token", None)
        if tok_condition in tokens_covered:
            continue
       
        results_one_condition = []
        for _ in range(repetitions):
            start = time()
            print(f"Evaluating conditioning for token: {tok_condition}")
            main_generate_inputs(domain, mode=mode, nb_concrete_inputs=num_inputs, 
                               token_condition=tok_condition)
            res_conditioned = run_multi_bug_eval_xml_on_folder(folder_path, allow_xxe=True)
            res_conditioned["conditioning_token"] = tok_condition
            results_one_condition.append(res_conditioned)
            tokens_covered.add(tok_condition)
            elapsed = time() - start
            print(f"Evaluation took {elapsed:.0f}s")
        
        results_conditioning.append(results_one_condition)

    # Special case: 5x EntityRef sequence
    results_one_condition = []
    tok_condition = ["EntityRef"] * 5
    for _ in range(repetitions):
        start = time()
        print("Evaluating conditioning for 5x EntityRef...")
        main_generate_inputs(domain, mode=mode, nb_concrete_inputs=num_inputs, 
                           token_condition=tok_condition)
        res_conditioned = run_multi_bug_eval_xml_on_folder(folder_path, allow_xxe=True)
        res_conditioned["conditioning_token"] = "5xEntityRef"
        results_one_condition.append(res_conditioned)
        elapsed = time() - start
        print(f"Evaluation took {elapsed:.0f}s")
    
    results_conditioning.append(results_one_condition)
    
    all_results["ExplainFuzz + conditioning"] = results_conditioning
    save_results_to_json(output_file_path, all_results)
    
    return all_results


######### MAIN EXECUTION #########

def run_all_sql_evaluations(domains, repetitions=3, num_inputs=10000):
    """Run all SQL evaluations for specified domains."""
    print("=" * 60)
    print("RUNNING SQL MULTI-BUG EVALUATIONS")
    print("=" * 60)
    
    for domain in domains:
        print(f"\n--- Evaluating {domain} ---")
        file_path = f"data/results/multi_bug_rate/results_multi_bug_{domain}.json"
        run_sql_multi_bug_evaluation(
            domain=domain,
            file_path=file_path,
            repetitions=repetitions,
            num_inputs=num_inputs
        )
    
    print("\n" + "=" * 60)
    print("RUNNING SQL CONDITIONING EVALUATIONS")
    print("=" * 60)
    
    for domain in domains:
        print(f"\n--- Conditioning evaluation for {domain} ---")
        run_sql_conditioning_evaluation(
            domain=domain,
            input_file_path=f"data/results/multi_bug_rate/results_multi_bug_{domain}.json",
            output_file_path=f"data/results/multi_bug_rate/results_multi_bug_{domain}_with_conditioning.json",
            num_inputs=num_inputs,
            repetitions=repetitions
        )


def run_all_xml_evaluations(domains, repetitions=3, num_inputs=10000):
    """Run all XML evaluations for specified domains."""
    print("=" * 60)
    print("RUNNING XML MULTI-BUG EVALUATIONS")
    print("=" * 60)
    
    for domain in domains:
        print(f"\n--- Evaluating {domain} ---")
        res_file = f"data/results/multi_bug_rate/XML/eval_multi_bug_{domain}.json"
        run_xml_multi_bug_evaluation(domain, res_file, num_inputs=num_inputs, repetitions=repetitions)
    
    print("\n" + "=" * 60)
    print("RUNNING XML CONDITIONING EVALUATIONS")
    print("=" * 60)
    
    for domain in domains:
        print(f"\n--- Conditioning evaluation for {domain} ---")
        input_file = f"data/results/multi_bug_rate/XML/eval_multi_bug_{domain}.json"
        output_file = f"data/results/multi_bug_rate/XML/eval_cond_{domain}.json"
        run_xml_conditioning_evaluation(
            domain=domain,
            input_file_path=input_file,
            output_file_path=output_file,
            num_inputs=num_inputs,
            repetitions=repetitions
        )


if __name__ == "__main__":
    # SQL domains
    sql_domains = ["SQL1A", "SQL2A", "SQL3A", "SQL4A"]
    run_all_sql_evaluations(sql_domains, repetitions=3, num_inputs=10000)
    
    # XML domains
    xml_domains = ["XML1", "XML2", "XML3", "XML4"]
    run_all_xml_evaluations(xml_domains, repetitions=3, num_inputs=10000)