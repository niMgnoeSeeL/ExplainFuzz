import torch
from GrammarRefactoring.refactor_grammar.checker import load_parser_lexer
from cfg2pc.main import anonymize_folder_inputs
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
    SEEDS_DIR,
    get_literal_token_mapping
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
    seeds_dir = SEEDS_DIR / domain
    parser_final_file_path = GRAMMAR_DIR / "final" / domain / f"{grammar_name}Parser.g4"
    antlr_output_dir = GEN_PARSER_DIR / domain
    print(antlr_output_dir)
    _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)
    seeds = anonymize_folder_inputs(
        seeds_dir, parser_final_file_path, start_rule, lexer_cls, skip_rules
    )
    results = []
    results_string = (
        f"--------------Evaluation inference for the domain {domain}------------ \n \n"
    )
    for mode in ["no-generate", "with-generate"]:
        results_string += f"###### Evaluation for the mode {mode} ######### \n \n "
        # Load model
        model_save_path = MODEL_DIR / domain / f"{domain}-{mode}-{max_length}.pt"
        model = torch.load(model_save_path, weights_only=False)
        model.eval()
        lit_map = model.lit_map
        lit_size = max(l for l in lit_map.values()) + 1

        print(seeds)

        # Evaluate inference for the different type of queries

        # # ##### MAR 1 ######
        toks_marginals = inference_inputs["MAR1"]
        res_list, res_str = eval_MAR1(
            model, lit_map, max_length, lit_size, toks_marginals, seeds, mode, domain
        )
        results += res_list
        results_string += res_str

        # # ##### COND 1 ######
        seqs_cond = inference_inputs["COND1"]
        res_list, res_str = eval_COND1(
            model, lit_map, max_length, lit_size, seqs_cond, seeds, mode, domain
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
            model, lit_map, max_length, lit_size, seqs_cond, seeds, mode, domain
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
    for tok in seqs:
        str_res += "--EVI QUERY FROM PC -- \n"
        prob_model = abs(evi_query(model, tok, lit_map, lit_size))
        str_res += f"P({tok})={prob_model:.4f} \n"

        str_res += "--EVI QUERY FROM SEEDS -- \n"
        prob_seeds = _evi_weights(tok, seeds)
        str_res += f"P({tok})={prob_seeds:.4f} \n \n"

        results.append(
            {
                "domain": domain,
                "mode": mode,
                "query_type": "EVI",
                "query": tok,
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
                "token": tok,
                "given_token": tok2,
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
    # Load your JSON from a file or directly as a string
    with open(file, "r") as f:
        data = json.load(f)

    # Structure to accumulate differences
    stats = defaultdict(lambda: defaultdict(list))  # stats[query_type][mode] = list of diffs
    all_modes = set()

    for domain, examples in data.items():
        for example_group in examples:
            for entry in example_group:
                mode = entry.get("mode")
                query_type = entry.get("query_type")
                model_prob = entry.get("model_prob")
                seed_prob = entry.get("seed_prob")

                # Some entries (like EVI) might not have token, but we only need probabilities
                if mode and query_type and model_prob is not None and seed_prob is not None:
                    diff = abs(model_prob - seed_prob)
                    stats[(domain, query_type)][mode].append(diff)
                    all_modes.add(mode)

    all_modes = sorted(all_modes)  # Consistent column order

     # Write LaTeX table
    with open("results_table.tex", "w") as f:
        f.write("\\begin{tabular}{ll" + "r" * len(all_modes) + "}\n")
        f.write("\\toprule\n")
        header = "Domain & Query Type"
        for mode in all_modes:
            header += f" & {mode}"
        header += " \\\\\n"
        f.write(header)
        f.write("\\midrule\n")

        for (domain, query_type), mode_diffs in sorted(stats.items()):
            row = f"{domain} & {query_type}"
            for mode in all_modes:
                diffs = mode_diffs.get(mode, [])
                avg_diff = sum(diffs) / len(diffs) if diffs else 0.0
                row += f" & {avg_diff:.4f}"
            row += " \\\\\n"
            f.write(row)

        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")

    print("LaTeX table saved to results_table.tex")

import json
def eval_mar1_tokens(domain, literals, save_path, mode="no-generate"):
    with open(save_path, "r") as f:
        all_res = json.load(f)
    
    valid_results = {}

    for lit in literals:
        try:
            valid_results[lit]=prob_MAR1(domain, lit, mode) 
        except Exception as e:
            pass

    all_res[domain]=valid_results

    with open(save_path, "w") as f:
        json.dump(all_res,f,indent=4)
    return all_res

def prob_MAR1(domain, lit, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    inputs = [token]
    query_type = "MAR1"
    prob = compute_probability(domain, query_type, inputs, mode)
    return prob


def generate_table_latex_mar1(input_file):
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
            row.append(f"{value:.2f}")
        latex += " & ".join(row) + " \\\\\n"

    latex += "\\end{tabular}"
    print(latex)


if __name__ == "__main__":
    # config_file_path = "domains_config.json"
    # domains_config = load_domains_config(config_file_path)

    # domains = ["SQL", "B", "JANUS", "REDIS"]

    # for domain in domains:
    #     domain_config = domains_config[domain]

    #     eval_inference_domain(
    #         domain,
    #         grammar_name=domain_config["grammar_name"],
    #         start_rule=domain_config["start_rule"],
    #         skip_rules=domain_config["skip_rules"],
    #         max_length=domain_config["max_length"],
    #         inference_inputs=domain_config["inference_inputs"],
    #         grammar_path=domain_config["parser_path"]
    #     )

    # file = RESULTS_DIR / "PC" / "eval_PC_inference.json"
    # analyze_results(file)


    # Evaluate MAR 1 probabilities for different SQL seeds
    literals = ["SELECT","FROM","WHERE","JOIN","ON","GROUP","ORDER","HAVING","NOT","UNION"]
    res_path = RESULTS_DIR / "SEEDS" / "eval_mar1_domains_SQL.json"
    for domain in ["SQL1A","SQL2A","SQL3A","SQL4A"]:
        print("Evaluating MAR1 tokens for domain",domain)
        eval_mar1_tokens(domain,literals,res_path)

    generate_table_latex_mar1(res_path)

        
