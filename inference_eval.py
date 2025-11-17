import torch
from GrammarRefactoring.refactor_grammar.checker import load_parser_lexer
from cfg2pc.main import parse_and_anonymize_folder_inputs
from cfg2pc.query import marginal_query, marginal_query_cond, marginal_query_contiguous_cond, evi_query, marginal_sequence_query, sequential_query_contiguous_cond, marginal_map_query
from cfg2pc.SQL_prob import marginal_proba, conditional_in_order, conditional_direct, _evi_weights, marginal_sequence, conditional_sequential, next_token
from evaluation import save_results
from collections import defaultdict
import json
from inference import compute_probability
from main import (
    GEN_PARSER_DIR,
    GRAMMAR_DIR,
    MODEL_DIR,
    RESULTS_DIR,
    DATASET_DIR,
    get_literal_token_mapping,
    load_domains_config
)


def save_results_string(results_string_path, results_string):
    with open(results_string_path, "r") as file:
        text = file.read()
    text += "\n \n"
    text = results_string
    with open(results_string_path, "w") as file:
        file.write(text)


def eval_inference_domain(
    domain, grammar_name, start_rule, skip_rules, max_length, inference_inputs, grammar_path
):
    # get the anonymized seeds
    
    #seeds_dir = SEEDS_DIR / domain
    # train_dataset_dir = DATASET_DIR / domain / mode / "train"
    parser_final_file_path = GRAMMAR_DIR / "final" / domain / f"{grammar_name}Parser.g4"
    antlr_output_dir = GEN_PARSER_DIR / domain
    
    _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)
    
    results = []
    results_string = (
        f"--------------Evaluation inference for the domain {domain}------------ \n \n"
    )
    print(f"Evaluation inference for the domain {domain}")
    for mode in ["no-generate"]:
        results_string += f"###### Evaluation for the mode {mode} ######### \n \n "

        train_dataset_dir = DATASET_DIR / domain / mode / "train"
        train_dataset = parse_and_anonymize_folder_inputs(
            train_dataset_dir, parser_final_file_path, start_rule, lexer_cls, skip_rules,max_length
        )
        print(train_dataset[:2])
        # Load model
        model_save_path = MODEL_DIR / domain / f"{domain}-{mode}-{max_length}.pt"
        model = torch.load(model_save_path, weights_only=False)
        model.eval()
        lit_map = model.lit_map
        lit_size = max(l for l in lit_map.values()) + 1

        # Evaluate inference for the different type of queries

        # # ##### MAR 1 ######
        toks_marginals = inference_inputs["MAR1"]
        res_list, res_str = eval_MAR1(
            model, lit_map, max_length, lit_size, toks_marginals, train_dataset, mode, domain
        )
        results += res_list
        results_string += res_str

        # # ##### COND 1 ######
        seqs_cond = inference_inputs["COND1"]
        res_list, res_str = eval_COND1(
            model, lit_map, max_length, lit_size, seqs_cond, train_dataset, mode, domain
        )
        results += res_list
        results_string += res_str

        # # ##### COND 2 ######
        # seqs_cond = inference_inputs["COND2"]
        # res_list, res_str = eval_COND2(
        #     model, lit_map, max_length, lit_size, seqs_cond, seeds, mode, domain
        # )
        # results += res_list
        # results_string += res_str

        #  ##### EVI ######
        seqs_cond = inference_inputs["EVI"]
        res_list, res_str = eval_EVI(
            model, lit_map, max_length, lit_size, seqs_cond, train_dataset, mode, domain
        )
        results += res_list
        results_string += res_str

        # # ##### MAR2 ######
        # seqs_cond = inference_inputs["COND1"]
        # res_list, res_str = eval_MAR_SEQ(
        #     model, lit_map, max_length, lit_size, seqs_cond, seeds, mode, domain
        # )
        # results += res_list
        # results_string += res_str

        # # ##### COND 3 ######
        # seqs_cond = inference_inputs["COND3"]
        # res_list, res_str = eval_COND_SEQ(
        #     model, lit_map, max_length, lit_size, seqs_cond, seeds, mode, domain
        # )
        # results += res_list
        # results_string += res_str

        # # ##### MAP ######
        # seqs_cond = inference_inputs["MAR1"]
        # res_list, res_str = eval_MAP(
        #     model, lit_map, max_length, lit_size, seqs_cond, seeds, mode, domain
        # )
        # results += res_list
        # results_string += res_str


    results_path = RESULTS_DIR / "PC"
    save_results(results_path, results, domain, "eval_PC_inference.json")

    results_string_path = RESULTS_DIR / "PC" / "results_inference.txt"
    save_results_string(results_string_path, results_string)

    print(results_string)


def eval_MAR1(model, lit_map, max_length, lit_size, toks, seeds, mode, domain):
    """
    MAR1 : P(token) ?
    """
    results = []
    str_res = ""
    for tok in toks:
        str_res += "--MARGINAL1 QUERY FROM PC -- \n"
        prob_model = abs(marginal_query(model, tok, lit_map, lit_size, max_length))
        str_res += f"P({tok})={prob_model:.4f} \n"

        str_res += "--MARGINAL1 QUERY FROM SEEDS -- \n"
        prob_seeds = marginal_proba(tok, seeds)
        str_res += f"P({tok})={prob_seeds:.4f} \n \n"

        results.append(
            {
                "domain": domain,
                "mode": mode,
                "query_type": "MAR1",
                "token": tok,
                "model_prob": prob_model,
                "seed_prob": prob_seeds,
            }
        )

    return results, str_res

def eval_EVI(model, lit_map, max_length, lit_size, seqs, seeds, mode, domain):
    """
    EVI : P(query == sequence) ?
    """
    results = []
    str_res = ""
    for seq in seqs:
        str_res += "--EVI QUERY FROM PC -- \n"
        prob_model = abs(evi_query(model, seq, lit_map, lit_size))
        str_res += f"P({seq})={prob_model:.4f} \n"

        str_res += "--EVI QUERY FROM SEEDS -- \n"
        prob_seeds = _evi_weights(seq+["EOF"], seeds)
        str_res += f"P({seq})={prob_seeds:.4f} \n \n"

        results.append(
            {
                "domain": domain,
                "mode": mode,
                "query_type": "EVI",
                "query": seq,
                "model_prob": prob_model,
                "seed_prob": prob_seeds,
            }
        )

    return results, str_res


def eval_COND1(model, lit_map, max_length, lit_size, seqs, seeds, mode, domain):
    """
    COND1 : P(token2|token1) ?
    """
    results = []
    str_res = ""
    for seq in seqs:
        tok = seq[0]
        tok2 = seq[1]

        str_res += " --CONDITIONAL QUERY 1 FROM PC -- \n"
        prob_model = abs(
            marginal_query_cond(model, tok, tok2, lit_map, lit_size, max_length)
        )
        str_res += f"P({tok2}|{tok})={prob_model:.4f} \n"

        str_res += "--CONDITIONAL QUERY 1 FROM SEEDS -- \n"
        prob_seeds = conditional_in_order(tok, tok2, seeds)
        str_res += f"P({tok2}|{tok})={prob_seeds:.4f} \n\n"

        results.append(
            {
                "domain": domain,
                "mode": mode,
                "query_type": "COND1",
                "token": tok2,
                "given_token": tok,
                "model_prob": prob_model,
                "seed_prob": prob_seeds,
            }
        )

    return results, str_res


def eval_COND2(model, lit_map, max_length, lit_size, seqs, seeds, mode, domain):
    """
    COND2 : P(token|sequence) ?
    """
    results = []
    str_res = ""
    for seq in seqs:
        tok = seq[0]
        tok2 = seq[1]

        str_res += " --CONDITIONAL QUERY 2 FROM PC -- \n"
        prob_model = abs(
            marginal_query_contiguous_cond(model, tok, tok2, lit_map, lit_size, max_length)
        )
        str_res += f"P({tok2}|{tok})={prob_model:.4f} \n"

        str_res += "--CONDITIONAL QUERY 2 FROM SEEDS -- \n"
        prob_seeds = conditional_direct(tok2, tok, seeds)
        str_res += f"P({tok2}|{tok})={prob_seeds:.4f} \n\n"

        results.append(
            {
                "domain": domain,
                "mode": mode,
                "query_type": "COND2",
                "token": tok,
                "given_token": tok2,
                "model_prob": prob_model,
                "seed_prob": prob_seeds,
            }
        )

    return results, str_res

def eval_MAR_SEQ(model, lit_map, max_length, lit_size, seqs, seeds, mode, domain):
    """
    MAR2 : P(sequence) ?
    """
    results = []
    str_res = ""
    for seq in seqs:
        str_res += "--MAR 2 QUERY FROM PC -- \n"
        prob_model = abs(marginal_sequence_query(model, seq, lit_map, lit_size, max_length))
        str_res += f"P({seq})={prob_model:.4f} \n"

        str_res += "--MAR 2 FROM SEEDS -- \n"
        prob_seeds = marginal_sequence(seq, seeds)
        str_res += f"P({seq})={prob_seeds:.4f} \n \n"

        results.append(
            {
                "domain": domain,
                "mode": mode,
                "query_type": "MAR2",
                "sequence": seq,
                "model_prob": prob_model,
                "seed_prob": prob_seeds,
            }
        )

    return results, str_res


def eval_COND_SEQ(model, lit_map, max_length, lit_size, seqs, seeds, mode, domain):
    """
    COND3 : P(token|sequence) ?
    """
    results = []
    str_res = ""
    for seq in seqs:
        tok = seq[len(tok)-1]
        sequence = seq[0:len(tok)-1]
        str_res += "-- CONDITIONAL 3 QUERY FROM PC -- \n"
        prob_model = abs(sequential_query_contiguous_cond(model, tok, sequence, lit_map, lit_size, max_length))
        str_res += f"P({tok|sequence})={prob_model:.4f} \n"

        str_res += "-- CONDITIONAL 3 SEQ FROM SEEDS -- \n"

        prob_seeds = conditional_sequential(sequence, tok, seeds)
        str_res += f"P({tok|sequence})={prob_seeds:.4f} \n \n"

        results.append(
            {
                "domain": domain,
                "mode": mode,
                "query_type": "COND3",
                "token": tok[len(tok)-1],
                "sequence": tok[0:len(tok)-1],
                "model_prob": prob_model,
                "seed_prob": prob_seeds,
            }
        )

    return results, str_res


def eval_MAP(model, lit_map, max_length, lit_size, toks, seeds, mode, domain):
    """
    MAP : P(token2|token1) ?
    """
    results = []
    str_res = ""
    for tok in toks:
    
        str_res += " -- MAP QUERY FROM PC -- \n"
        selection_model = marginal_map_query(model, tok, lit_map, lit_size, max_length)
   
        str_res += f"P({tok})={selection_model} \n"

        str_res += "-- MAP QUERY FROM SEEDS -- \n"
        selection_seeds = next_token(tok, seeds)
        str_res += f"P({tok})={selection_seeds} \n\n"

        results.append(
            {
                "domain": domain,
                "mode": mode,
                "query_type": "MAP",
                "token": tok,
                "model_selection": selection_model,
                "seed_selection": selection_seeds,
            }
        )

    return results, str_res


def analyze_results(file):
    # Load your JSON from a file
    with open(file, "r") as f:
        data = json.load(f)

    # Structure to accumulate model and ground-truth probabilities
    stats = defaultdict(lambda: {"gt": [], "mae": []})  # stats[(domain, query_type)] = {"gt": [...], "mae": [...]}

    for domain, examples in data.items():
        for example_group in examples:
            for entry in example_group:
                query_type = entry.get("query_type")
                model_prob = entry.get("model_prob")
                seed_prob = entry.get("seed_prob")

                if query_type is not None and model_prob is not None and seed_prob is not None:
                    diff = abs(model_prob - seed_prob)
                    stats[(domain, query_type)]["gt"].append(seed_prob)
                    stats[(domain, query_type)]["mae"].append(diff)

    # Write LaTeX table
    with open("data/results/PC/results_inference_table.tex", "w") as f:
        f.write("\\begin{tabular}{llrr}\n")
        f.write("\\toprule\n")
        f.write("\\textbf{Domain} & \\textbf{Query Type} & \\textbf{Mean GT} & \\textbf{MAE} \\\\\n")
        f.write("\\midrule\n")

        for (domain, query_type), values in sorted(stats.items()):
            mean_gt = sum(values["gt"]) / len(values["gt"]) if values["gt"] else 0.0
            mae = sum(values["mae"]) / len(values["mae"]) if values["mae"] else 0.0
            row = f"{domain} & {query_type} & {mean_gt:.4f} & {mae:.4f} \\\\\n"
            f.write(row)

        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")

    print("LaTeX table saved to results_table.tex")


def eval_mar1_tokens(domain, literals, save_path, mode="no-generate",is_token=False):
    try:
        with open(save_path, "r") as f:
            all_res = json.load(f)
    except:
        all_res={}
    
    valid_results = {}

    for lit in literals:
        try:
            valid_results[lit]=prob_MAR1(domain, lit, mode,is_token) 
        except Exception as e:
            pass

    all_res[domain]=valid_results

    with open(save_path, "w") as f:
        json.dump(all_res,f,indent=4)
    return all_res

def prob_MAR1(domain, lit, mode,is_token=False):
    if not is_token:
        literal_to_tokens = get_literal_token_mapping(domain)
        token = literal_to_tokens[lit]
    else:
        token=lit
    inputs = [token]
    query_type = "MAR1"
    prob = compute_probability(domain, query_type, inputs, mode)
    return prob

def eval_cond1_tokens(domain, literals, save_path, mode="no-generate",is_token=False):
    try:
        with open(save_path, "r") as f:
            all_res = json.load(f)
    except:
        all_res={}
    
    valid_results = all_res.get(domain,{})

    for (lit1,lit2) in literals:
        try:
            valid_results[lit2+'|'+lit1]=prob_COND1(domain, lit1,lit2, mode,is_token) 
        except Exception as e:
            print(e)
            pass

    all_res[domain]=valid_results

    with open(save_path, "w") as f:
        json.dump(all_res,f,indent=4)
    return all_res

def prob_COND1(domain, lit1,lit2, mode,is_token=False):
    if not is_token:
        literal_to_tokens = get_literal_token_mapping(domain)
        tok1,tok2 = literal_to_tokens[lit1],literal_to_tokens[lit2]
    else:
        tok1,tok2=lit1,lit2
    inputs = [tok1,tok2]
    query_type = "COND1"
    prob = compute_probability(domain, query_type, inputs, mode)
    return prob

def generate_table_latex_distribution_seeds(input_file):
    with open(input_file, "r") as f:
        data = json.load(f)
    # Get all literals (row labels)
    literals = list(next(iter(data.values())).keys())
    domains = list(data.keys())

    # Start LaTeX table
    latex = "\\begin{tabular}{l" + "c" * len(domains) + "}\n"
    latex += "Literal & " + " & ".join(domains) + " \\\\\n"
    latex += "\\hline\n"

    # Fill table rows
    for literal in literals:
        row = [f'P("{literal}")']
        for domain in domains:
            value = round(data[domain][literal], 2)
            row.append(f"\\heatcolor{{{value:.2f}}}")
        latex += " & ".join(row) + " \\\\\n"

    latex += "\\end{tabular}"
    print(latex)

def compute_xml_nested_structure_proba(domain,save_path,mode="no-generate"):
    p_slash = prob_MAR1(domain, "SLASH", mode,is_token=True) 
    p_slash_close = prob_MAR1(domain, "SLASH_CLOSE", mode,is_token=True) 
    p_slash_cond_slash = prob_COND1(domain, "SLASH","SLASH", mode,is_token=True) 
    p_slash_cond_slash_close = prob_COND1(domain, "SLASH_CLOSE","SLASH", mode,is_token=True)
    p_nested_structure = p_slash * p_slash_close + p_slash_cond_slash * p_slash_cond_slash_close

    with open(save_path, "r") as f:
        all_res = json.load(f)
    valid_results = all_res.get(domain,{})
    valid_results["nested structure"] = p_nested_structure

    with open(save_path, "w") as f:
        json.dump(all_res,f,indent=4)
    return all_res

###### MAIN FUNCTIONS TO RUN THE DIFFERENT EVAL #####

def run_eval_mar1_cond1_sql():
    literals = ["SELECT","FROM","WHERE","JOIN","GROUP","ORDER","HAVING","UNION"]
    cond_literals = [["SELECT","SELECT"]]
    res_path = RESULTS_DIR / "SEEDS" / "eval_mar1_domains_SQL.json"
    for domain in ["SQL1A","SQL2A","SQL3A","SQL4A"]:
        print("Evaluating MAR1 and COND1 tokens for domain",domain)
        eval_mar1_tokens(domain,literals,res_path)
        eval_cond1_tokens(domain,cond_literals,res_path)
    generate_table_latex_distribution_seeds(res_path)

def run_eval_mar1_cond1_xml():
    tokens = ["Name","CDATA","COMMENT","EntityRef"]
    res_path = RESULTS_DIR / "SEEDS" / "eval_mar1_domains_XML.json"
    domains = ["XML1","XML2","XML3","XML4"]
    for domain in domains:
        print("Evaluating MAR1 tokens for domain",domain)
        eval_mar1_tokens(domain,tokens,res_path,is_token=True)
        compute_xml_nested_structure_proba(domain,res_path)
    generate_table_latex_distribution_seeds(res_path)

def run_eval_inference():
    config_file_path = "domains_config.json"
    domains_config = load_domains_config(config_file_path)

    domains = ["SQL", "B", "JANUS", "REDIS"]
    for domain in domains:
        domain_config = domains_config[domain]

        eval_inference_domain(
            domain,
            grammar_name=domain_config["grammar_name"],
            start_rule=domain_config["start_rule"],
            skip_rules=domain_config["skip_rules"],
            max_length=domain_config["max_length"],
            inference_inputs=domain_config["inference_inputs"],
            grammar_path=domain_config["parser_path"]
        )

    file = RESULTS_DIR / "PC" / "eval_PC_inference.json"
    analyze_results(file)


if __name__ == "__main__":
    # ## EVAL INFERENCE
    # run_eval_inference()

    ## Evaluate MAR1 and COND1 probabilities for different SQL seeds
    run_eval_mar1_cond1_sql()

    # ## Evaluate MAR1 and COND1 probabilities for different XML seeds
    # run_eval_mar1_cond1_xml()


        
