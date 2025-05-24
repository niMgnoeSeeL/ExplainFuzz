import torch
from GrammarRefactoring.refactor_grammar.checker import load_parser_lexer
from cfg2pc.main import anonymize_folder_inputs
from cfg2pc.query import marginal_query, marginal_query_cond
from cfg2pc.SQL_prob import marginal_proba, conditional_in_order
from evaluation import save_results
from main import (
    GEN_PARSER_DIR,
    GRAMMAR_DIR,
    MODEL_DIR,
    RESULTS_DIR,
    SEEDS_DIR,
    load_domains_config,
)


def save_results_string(results_string_path, results_string):
    with open(results_string_path, "r") as file:
        text = file.read()
    text += "\n \n"
    text += results_string
    with open(results_string_path, "w") as file:
        file.write(text)


def eval_inference_domain(
    domain, grammar_name, start_rule, skip_rules, max_length, inference_inputs
):
    # get the anonymized seeds
    seeds_dir = SEEDS_DIR / domain
    parser_final_file_path = GRAMMAR_DIR / "final" / domain / f"{grammar_name}Parser.g4"
    antlr_output_dir = GEN_PARSER_DIR / domain
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

        # Evaluate inference for the different type of queries

        ##### MAR 1 ######
        toks_marginals = inference_inputs["MAR1"]
        res_list, res_str = eval_MAR1(
            model, lit_map, max_length, lit_size, toks_marginals, seeds, mode, domain
        )
        results += res_list
        results_string += res_str

        ##### COND 1 ######
        seqs_cond = inference_inputs["COND1"]
        res_list, res_str = eval_COND1(
            model, lit_map, max_length, lit_size, seqs_cond, seeds, mode, domain
        )
        results += res_list
        results_string += res_str

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
        str_res += "--MARGINAL QUERY FROM PC -- \n"
        prob_model = abs(marginal_query(model, tok, lit_map, lit_size, max_length))
        str_res += f"P({tok})={prob_model:.4f} \n"

        str_res += "--MARGINAL QUERY FROM SEEDS -- \n"
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


def eval_COND1(model, lit_map, max_length, lit_size, seqs, seeds, mode, domain):
    """
    COND1 : P(token2|token1) ?
    """
    results = []
    str_res = ""
    for seq in seqs:
        tok = seq[0]
        tok2 = seq[1]

        str_res += " --CONDITIONAL QUERY FROM PC -- \n"
        prob_model = abs(
            marginal_query_cond(model, tok, tok2, lit_map, lit_size, max_length)
        )
        str_res += f"P({tok2}|{tok})={prob_model:.4f} \n"

        str_res += "--CONDITIONAL QUERY FROM SEEDS -- \n"
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


if __name__ == "__main__":
    config_file_path = "domains_config.json"
    domains_config = load_domains_config(config_file_path)

    domain = "SQL"
    domain_config = domains_config[domain]

    eval_inference_domain(
        domain,
        grammar_name=domain_config["grammar_name"],
        start_rule=domain_config["start_rule"],
        skip_rules=domain_config["skip_rules"],
        max_length=domain_config["max_length"],
        inference_inputs=domain_config["inference_inputs"],
    )
