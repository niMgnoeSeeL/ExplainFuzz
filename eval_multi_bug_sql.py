from bug_specs import BUG_SPECS_SQL
from custom_generator_sql.schema import retrieve_schema
from grammarinator_fuzzing.filter_inputs import measure_multi_bug_rate, measure_multi_bug_rate_from_folder, read_queries_from_file
from main import RESULTS_DIR, get_literal_token_mapping, main_generate_inputs
import json


def eval_multi_bug_rate(source: str, path: str, from_file: bool = False,bug_specs={}, scenario=1,tok_condition=None):
    """
    Evaluate multi-bug rate for a given data source.

    Args:
        source (str): Name of the source (e.g., 'Grammarinator', 'ExplainFuzz', 'Seeds')
        path (str): Path to folder or file
        from_file (bool): Whether to read from a single file or from a folder
    """
    print(f"Evaluating {source}...")

    if from_file:
        print(f"Reading the file : {path}")
        queries = read_queries_from_file(path)
        res = measure_multi_bug_rate(queries,bug_specs,scenario,tok_condition)
    else:
        res = measure_multi_bug_rate_from_folder(path,bug_specs,scenario)

    return res


# Convenience wrappers for readability
def eval_multi_bug_rate_Grammarinator(scenario,folder_path):
    return eval_multi_bug_rate(
        source="Grammarinator",
        path=folder_path,
        from_file=False,
        bug_specs=BUG_SPECS_SQL,
         scenario=scenario
    )

def eval_multi_bug_rate_ExplainFuzz(domain,scenario,tok_condition=None):
    return eval_multi_bug_rate(
        source="ExplainFuzz",
        path=f"data/output/inputs/{domain}/inputs_no_generate.txt",
        from_file=True,
        bug_specs=BUG_SPECS_SQL,
         scenario=scenario,
         tok_condition=tok_condition
    )

def eval_multi_bug_rate_seeds(domain,scenario):
    domain_seeds = domain[:-1] if domain[-1]=="A" or domain[-1]=="B" else domain
    return eval_multi_bug_rate(
        source="Seeds",
        path=f"data/input/seeds/{domain_seeds}/",
        from_file=False,
        bug_specs =BUG_SPECS_SQL,
        scenario=scenario
    )


def run_eval_multi_bug(domain="SQL",mode="no-generate",num_inputs=10000,R=5,file_path=None,scenario=2):
    results = {}
    res_Seeds = eval_multi_bug_rate_seeds(domain,scenario)
    res_grammarinator = run_eval_Grammarinator(domain)
    res_ExplainFuzz = []
    for _ in range(R):
        main_generate_inputs(domain, mode, num_inputs,None)
        res_ExplainFuzz_k = eval_multi_bug_rate_ExplainFuzz(domain,scenario)
        res_ExplainFuzz.append(res_ExplainFuzz_k)

    results["Seeds"] = res_Seeds
    results["Grammarinator"]=res_grammarinator
    results["ExplainFuzz"]=res_ExplainFuzz
    
    if not file_path:
        file_name = f"results_multi_bug_{domain}.json"
        folder_path = RESULTS_DIR / "bug_rate"
        file_path =  folder_path / file_name

    with open(file_path, "w") as f:
        json.dump(results, f, indent=4, default=str)
    
    print(f"🎉 Evaluation complete. Results saved to {file_path}")

    return results

def run_eval_Grammarinator(domain):
    scenario = 2
    results_gram = []
    for try_id in range(1,4):
        folder_path = f"data/intermediate/fuzz_outputs/{domain}/try-{try_id}/no-generate/"
        res_gramm = eval_multi_bug_rate_Grammarinator(scenario,folder_path)
        results_gram.append(res_gramm)
    
    return results_gram

def run_eval_conditioning(domain,res_file_path,save_file_path,nb_inputs=10000,R=3):
    all_res={}
    with open(res_file_path, "r") as f:
        all_res = json.load(f)
    literal_to_tokens = get_literal_token_mapping(domain)
    results_conditioning=[]
    tokens_covered = set()
    
    conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"
    schema = retrieve_schema(conninfo)

    for _,bug_info in BUG_SPECS_SQL.items():
        required_tokens = bug_info["required"]
        lit_condition = required_tokens[0] if required_tokens else None
        tok_condition = literal_to_tokens.get(lit_condition,None)
        if tok_condition in tokens_covered:
            continue
       
        results_one_condition=[]
        for _ in range(R):
            print(f"Evaluating conditioning for tok condition {tok_condition}...")
            main_generate_inputs(
                domain=domain,
                mode="no-generate",
                nb_concrete_inputs=nb_inputs,
                token_condition=tok_condition,
                dry_run=True,
                schema=schema
            )
            res_conditioned = eval_multi_bug_rate_ExplainFuzz(domain,scenario=2,tok_condition=lit_condition)
            res_conditioned["conditioning_token"] = lit_condition
            results_one_condition.append(res_conditioned)
            tokens_covered.add(tok_condition)
        results_conditioning.append(results_one_condition)

    all_res["ExplainFuzz + conditioning"] = results_conditioning
    with open(save_file_path, "w") as f:
        json.dump(all_res, f, indent=4)
    
    ###### To add conditioning on the token UNION afterwards
    # all_res={}
    # with open(save_file_path, "r") as f:
    #     all_res = json.load(f)
    # results_conditioning=all_res["ExplainFuzz + conditioning"]
    
    # conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"
    # schema = retrieve_schema(conninfo)
   
    # tok_condition = "UNION"
    # lit_condition = "UNION"
    # results_one_condition=[]
    # for _ in range(R):
    #     print(f"Evaluating conditioning for tok condition nested select...")
    #     main_generate_inputs(
    #         domain=domain,
    #         mode="no-generate",
    #         nb_concrete_inputs=nb_inputs,
    #         token_condition=tok_condition,
    #         dry_run=True,
    #         schema=schema
    #     )
    #     res_conditioned = eval_multi_bug_rate_ExplainFuzz(domain,scenario=2,tok_condition=lit_condition)
    #     res_conditioned["conditioning_token"] = lit_condition
    #     results_one_condition.append(res_conditioned)
    # results_conditioning.append(results_one_condition)
        
    
    # all_res["ExplainFuzz + conditioning"] = results_conditioning
    # with open(save_file_path, "w") as f:
    #     json.dump(all_res, f, indent=4)
    
    return all_res

if __name__ == "__main__":
    domains = ["SQL1A","SQL2A","SQL3A","SQL4A"]
    # RUNNING THE MULTI BUG EVAL
    for domain in domains:
        file_path = f"data/results/multi_bug_rate/results_multi_bug_{domain}.json"
        results= run_eval_multi_bug(file_path = file_path,R=3,domain=domain)
    
    # RUNNING CONDITIONING EVALUATION
    for domain in domains:
        all_res = run_eval_conditioning(
            domain,
            f"data/results/multi_bug_rate/results_multi_bug_{domain}.json",
            f"data/results/multi_bug_rate/results_multi_bug_{domain}_with_conditioning.json",
            nb_inputs=10000,
            R=3
        )
