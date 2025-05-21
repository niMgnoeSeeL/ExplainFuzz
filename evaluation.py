from GrammarRefactoring.main import analyze_antlr_grammar
import json
from pathlib import Path

from GrammarRefactoring.refactor_grammar.checker import load_parser_lexer
from cfg2pc.evaluate_llm import get_res_evaluation
from cfg2pc.evaluation_seeds import compute_metrics_seeds
from cfg2pc.main import anonymize_folder_inputs, main_build_train_model
from cfg2pc.pcfg import run_pcfg
from main import (
    DATASET_DIR,
    GEN_PARSER_DIR,
    GRAMMAR_DIR,
    MODEL_DIR,
    RESULTS_DIR,
    SEEDS_DIR,
    ensure_directories_exist,
    load_domains_config,
)
import multiprocessing


def save_results(
    results_path: Path, new_result: dict, domain: str, filename: str = "results.json"
):
    """
    Save a new grammar analysis result into a JSON file.
    If the file exists, it appends the result to the list.
    If not, it creates a new list with the result.
    """
    results_path.mkdir(parents=True, exist_ok=True)
    file_path = results_path / filename

    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    if domain in data:
        data[domain].append(new_result)
    else:
        data[domain] = [new_result]

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def evaluate_grammar(domain, grammar_name):
    parser_final_file_path = GRAMMAR_DIR / "final" / domain / f"{grammar_name}Parser.g4"
    grammar_metrics = analyze_antlr_grammar(parser_final_file_path)
    grammar_metrics["domain"] = domain
    results_grammar_dir = RESULTS_DIR / "grammars"
    save_results(results_grammar_dir, grammar_metrics, domain, "results_grammars.json")


def evaluate_PCFG(
    lengths,
    domain,
    grammar_name,
    start_rule,
    skip_rules,
):
    modes = ["no-generate", "with-generate"]
    results_pcfg_dir = RESULTS_DIR / "PCFG"
    dataset_dir = DATASET_DIR / domain
    antlr_output_dir = GEN_PARSER_DIR / domain
    grammar_path = GRAMMAR_DIR / "final" / domain / f"{grammar_name}Parser.g4"
    _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)
    for max_length in lengths:
        for mode in modes:
            test_dataset = dataset_dir / mode / "test"
            train_dataset = dataset_dir / mode / "train"
            res = run_pcfg(
                domain,
                max_length,
                train_dataset,
                test_dataset,
                grammar_path,
                start_rule,
                mode,
                lexer_cls,
                skip_rules,
            )

            save_results(results_pcfg_dir, res, domain, "eval_PCFG.json")


def get_seeds_anonymized(domain, grammar_name, grammar_path, start_rule, skip_rules):
    seeds_path = SEEDS_DIR / domain
    antlr_output_dir = GEN_PARSER_DIR / domain
    _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)
    seeds_anonymized = anonymize_folder_inputs(
        seeds_path, grammar_path, start_rule, lexer_cls, skip_rules
    )
    return seeds_anonymized


def evaluate_seeds(domain, grammar_name, start_rule, skip_rules):
    grammar_path = GRAMMAR_DIR / "final" / domain / f"{grammar_name}Parser.g4"
    seeds_anonymized = get_seeds_anonymized(
        domain, grammar_name, grammar_path, start_rule, skip_rules
    )
    res = compute_metrics_seeds(seeds_anonymized, domain)
    results_seeds_dir = RESULTS_DIR / "SEEDS"
    save_results(results_seeds_dir, res, domain, "eval_seeds.json")
    return res["max_sequence_length"]


def evaluate_llm(lengths, domain, grammar_name, start_rule, skip_rules):
    modes = ["no-generate", "with-generate"]
    grammar_path = GRAMMAR_DIR / "final" / domain / f"{grammar_name}Parser.g4"
    dataset_dir = DATASET_DIR / domain
    results_llm_dir = RESULTS_DIR / "LLM"
    antlr_output_dir = GEN_PARSER_DIR / domain
    _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)
    seeds_anonymized = get_seeds_anonymized(
        domain, grammar_name, grammar_path, start_rule, skip_rules
    )
    for max_length in lengths:
        for mode in modes:
            test_dataset = dataset_dir / mode / "test"
            res = get_res_evaluation(
                max_length,
                mode,
                domain,
                test_dataset,
                grammar_path,
                seeds_anonymized,
                start_rule,
                lexer_cls,
                skip_rules,
            )

            save_results(results_llm_dir, res, domain, "eval_llm.json")


def run_model_with_timeout(queue, *args):
    try:
        pc_metrics = main_build_train_model(*args)
        queue.put(pc_metrics)
    except Exception as e:
        queue.put({"error": str(e)})


def evaluate_PC(
    domain, grammar_name, start_rule, max_seeds_length, skip_rules, max_time
):
    nb_epochs = 10
    model_save_dir = MODEL_DIR / domain
    dataset_dir = DATASET_DIR / domain
    antlr_output_dir = GEN_PARSER_DIR / domain
    parser_final_file_path = GRAMMAR_DIR / "final" / domain / f"{grammar_name}Parser.g4"

    lengths_success = []
    for mode in ["no-generate", "with-generate"]:
        for max_length in range(5, max_seeds_length + 10, 5):
            print(
                f"--> Building the PC for the mode {mode.replace('-', ' ')} and max sequence length {max_length}"
            )
            model_save_path = model_save_dir / f"{domain}-{mode}-{max_length}.pt"
            trainingset_dir = dataset_dir / mode / "train"
            testingset_dir = dataset_dir / mode / "test"
            ensure_directories_exist([model_save_dir, trainingset_dir, testingset_dir])
            _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)

            queue = multiprocessing.Queue()
            args = (
                parser_final_file_path,
                start_rule,
                trainingset_dir,
                model_save_path,
                max_length,
                lexer_cls,
                nb_epochs,
                testingset_dir,
                skip_rules,
            )

            p = multiprocessing.Process(
                target=run_model_with_timeout, args=(queue, *args)
            )
            p.start()
            p.join(timeout=max_time)

            if p.is_alive():
                print(f"⏱ Timeout reached ({max_time}s) — terminating the process.")
                p.terminate()
                p.join()
                break  # Skip this configuration

            result = queue.get()
            if "error" in result:
                print("❌ Error during model training:", result["error"])
                continue

            pc_metrics = result
            pc_metrics["domain"] = domain
            pc_metrics["mode"] = mode
            pc_metrics["max_length"] = max_length

            results_pc_dir = RESULTS_DIR / "PC"
            save_results(results_pc_dir, pc_metrics, domain, "eval_PC_model.json")
            lengths_success.append(max_length)

    return lengths_success


def evaluate_one_domain(
    domain,
    grammar_name,
    start_rule,
    skip_rules,
):
    print(f"##### EVALUATION OF THE DOMAIN {domain} ########")
    print("")

    # ##### EVALUATE SEEDS #######
    print("-> Evaluation the seeds")
    max_seeds_length = evaluate_seeds(domain, grammar_name, start_rule, skip_rules)

    # ##### EVALUATE GRAMMAR ######
    print("-> Evaluating the Grammar")
    evaluate_grammar(domain, grammar_name)

    #### EVALUATE PC COMPILATION AND TRAINING #######

    print("->Evaluating the PC compilation and training")
    lengths = evaluate_PC(
        domain,
        grammar_name,
        start_rule,
        max_seeds_length,
        skip_rules,
        max_time=1500,
    )

    ###### EVALUATE PCFG ######
    print("-> Evaluation PCFG training")
    evaluate_PCFG(
        lengths,
        domain,
        grammar_name,
        start_rule,
        skip_rules,
    )

    ###### EVALUATE LLM #######
    print("-> Evaluating LLM ")
    evaluate_llm(lengths, domain, grammar_name, start_rule, skip_rules)


if __name__ == "__main__":
    config_file_path = "domains_config.json"
    domains_config = load_domains_config(config_file_path)
    domain = "JANUS"
    domain_config = domains_config[domain]
    evaluate_one_domain(
        domain,
        domain_config["grammar_name"],
        domain_config["start_rule"],
        domain_config["skip_rules"],
    )
