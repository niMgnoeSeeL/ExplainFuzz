from grammarinator_fuzzing.main import main as grammar_fuzz_main
from custom_generator_sql.main import main as custom_gen_sql_main
from GrammarRefactoring.main import (
    analyze_antlr_grammar,
    refactor_grammar as grammar_refactoring_main,
)
from GrammarRefactoring.refactor_grammar.checker import load_parser_lexer
from pathlib import Path

from cfg2pc.main import main_build_train_model, main_sampling
import json
import multiprocessing


# === Global Path Variables ===
BASE_DIR = Path("data")
INTERMEDIATE_DIR = BASE_DIR / "intermediate"
OUTPUT_DIR = BASE_DIR / "output"
INPUT_DIR = BASE_DIR / "input"
GENERATED_DIR = INTERMEDIATE_DIR / "generated"
GRAMMAR_DIR = INTERMEDIATE_DIR / "grammars"
GRAMMAR_FINAL_DIR = GRAMMAR_DIR / "final"
GENERATOR_DIR = GENERATED_DIR / "generator"
POPULATION_DIR = GENERATED_DIR / "population"
GEN_PARSER_DIR = GENERATED_DIR / "parser"
FUZZ_OUTPUTS_DIR = INTERMEDIATE_DIR / "fuzz_outputs"
DATASET_DIR = INTERMEDIATE_DIR / "dataset"
SEEDS_DIR = INPUT_DIR / "seeds"
MODEL_DIR = OUTPUT_DIR / "model"
SAMPLES_DIR = INTERMEDIATE_DIR / "samples"
RESULTS_DIR = BASE_DIR / "results"


def ensure_directories_exist(directories):
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def save_results(results_path: Path, new_result: dict, filename: str = "results.json"):
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
        data = []

    data.append(new_result)

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def fuzzing_campaign(prefix_grammar, domain, start_rule):
    grammar_fuzz_main(
        prefix_grammar=prefix_grammar,
        domain=domain,
        start_rule=start_rule,
        num_inputs=10,
        first_time=True,
    )


def build_model(
    domain,
    grammar_name,
    initial_grammar_paths,
    max_length,
    start_rule=None,
    num_inputs=10,
    skip_rules=[],
    with_serializer=False,
):
    # Create necessary directories
    required_dirs = [
        BASE_DIR,
        INTERMEDIATE_DIR,
        OUTPUT_DIR,
        GENERATED_DIR,
        GRAMMAR_DIR,
        GRAMMAR_FINAL_DIR,
        GENERATOR_DIR,
        POPULATION_DIR,
        GEN_PARSER_DIR,
        FUZZ_OUTPUTS_DIR,
        DATASET_DIR,
        SEEDS_DIR,
        MODEL_DIR,
        SAMPLES_DIR,
        RESULTS_DIR,
    ]
    ensure_directories_exist(required_dirs)

    print("-----Refactoring the grammar----\n")
    intermediate_dir = GRAMMAR_DIR / "intermediate" / domain
    refactored_dir = GRAMMAR_DIR / "refactored" / domain
    final_dir = GRAMMAR_DIR / "final" / domain
    antlr_output_dir = GEN_PARSER_DIR / domain
    seeds_dir = SEEDS_DIR / domain

    refactoring_dirs = [
        intermediate_dir,
        refactored_dir,
        final_dir,
        antlr_output_dir,
        seeds_dir,
    ]
    ensure_directories_exist(refactoring_dirs)

    grammar = grammar_refactoring_main(
        initial_grammar_paths,
        grammar_name,
        intermediate_dir,
        refactored_dir,
        final_dir,
        antlr_output_dir,
        seeds_dir,
        start_rule,
    )

    # Analyze the grammar - compute metrics
    parser_final_file_path = final_dir / f"{grammar_name}Parser.g4"
    grammar_metrics = analyze_antlr_grammar(parser_final_file_path)
    grammar_metrics["domain"] = domain
    results_grammar_dir = RESULTS_DIR / "grammars"
    save_results(results_grammar_dir, grammar_metrics, "results_grammars.json")
    print("")

    # Fuzzing campaign
    print("-----Fuzzing Campaign-----")
    print("")

    generator_dir = GENERATOR_DIR / domain
    population_dir = POPULATION_DIR / domain
    fuzz_outputs_dir = FUZZ_OUTPUTS_DIR / domain
    dataset_dir = DATASET_DIR / domain
    fuzzing_dirs = [generator_dir, population_dir, fuzz_outputs_dir, dataset_dir]
    ensure_directories_exist(fuzzing_dirs)

    grammar_fuzz_main(
        prefix_grammar=grammar_name,
        start_rule=start_rule,
        grammar_dir=final_dir,
        seeds_dir=seeds_dir,
        generator_dir=generator_dir,
        population_dir=population_dir,
        gen_parser_dir=antlr_output_dir,
        fuzz_outputs_dir=fuzz_outputs_dir,
        dataset_dir=dataset_dir,
        num_inputs=num_inputs,
        first_time=True,
        with_serializer=with_serializer,
    )
    print("")

    # Build PC model
    print("-----Building the Probabilistic Circuit----")

    nb_epochs = 10
    model_save_dir = MODEL_DIR / domain

    for mode in ["no-generate", "with-generate"]:
        print(
            f"--> Building the PC for the mode {mode.replace('-', ' ')} and max sequence length {max_length}"
        )
        model_save_path = model_save_dir / f"{domain}-{mode}-{max_length}.pt"
        trainingset_dir = dataset_dir / mode / "train"
        testingset_dir = dataset_dir / mode / "test"
        ensure_directories_exist([model_save_dir, trainingset_dir, testingset_dir])
        _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)

        pc_metrics = main_build_train_model(
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
        pc_metrics["domain"] = domain
        pc_metrics["mode"] = mode
        pc_metrics["max_length"] = max_length

        results_pc_dir = RESULTS_DIR / "PC"
        save_results(results_pc_dir, pc_metrics, "results_PC_model.json")


def run_model_with_timeout(queue, *args):
    try:
        pc_metrics = main_build_train_model(*args)
        queue.put(pc_metrics)
    except Exception as e:
        queue.put({"error": str(e)})


def evaluate_PC(
    domain,
    dataset_dir,
    grammar_name,
    antlr_output_dir,
    parser_final_file_path,
    max_time,
):
    nb_epochs = 10
    model_save_dir = MODEL_DIR / domain

    for mode in ["no-generate", "with-generate"]:
        for max_length in range(40, 100, 5):
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
                trainingset_dir,
                model_save_path,
                max_length,
                lexer_cls,
                nb_epochs,
                testingset_dir,
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
            save_results(results_pc_dir, pc_metrics, "eval_PC_model.json")


def get_pre_trained_model(domain, mode, save_model_dir):
    model = ""
    return model


def inference(model):
    "Make inference"
    return


def concretization(conninfo, anonymized_queries, output_path):
    max_queries = 100
    length_batch = 20
    return custom_gen_sql_main(
        conninfo,
        anonymized_queries,
        output_path,
        max_queries,
        length_batch,
        dry_run=False,
    )


def sample_inputs(domain, mode, nb_inputs, max_length):
    model_save_path = MODEL_DIR / domain / f"{domain}-{mode}-{max_length}.pt"
    output_dir = SAMPLES_DIR / domain / mode
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"anonymized_inputs_{mode.replace('-','_')}.txt"
    main_sampling(model_save_path, nb_inputs, output_path)


# def generate_inputs(model, domain, mode):
#     sample_inputs(model)

#     conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"

#     input_file_name = f"anonymized_queries_{mode.replace('-','_')}.txt"
#     query_input = INTERMEDIATE_DIR / "anonymized" / domain / input_file_name
#     output_file_name = f"valid_inputs_{mode.replace('-','_')}.txt"
#     output_dir = OUTPUT_DIR / domain
#     output_dir.mkdir(parents=True, exist_ok=True)
#     output_path = output_dir / output_file_name

#     success_rate = concretization(conninfo, query_input, output_path)

#     custom_gen_sql_main(
#         conninfo,
#         query_input,
#         output_path,
#         max_queries=100,
#         length_batch=20,
#         dry_run=False,
#     )

#     return output_path, success_rate


if __name__ == "__main__":
    # domain = "XML"
    # grammar_name = "XML"
    # start_rule = "document"
    # parser_path = Path("data/input/grammars/XML/XMLParser.g4")
    # lexer_path = Path("data/input/grammars/XML/XMLLexer.g4")
    # seeds_dir = SEEDS_DIR / domain
    # initial_grammar_paths = [parser_path, lexer_path]
    # load_pc = None

    # domain = "HTML"
    # grammar_name = "HTML"
    # start_rule = "htmlDocument"
    # parser_path = Path("data/input/grammars/HTML/HTMLParser.g4")
    # lexer_path = Path("data/input/grammars/HTML/HTMLLexer.g4")
    # seeds_dir = SEEDS_DIR / domain
    # initial_grammar_paths = [parser_path, lexer_path]

    ####### WORKING DOMAINS ######
    # domain = "REDIS"
    # grammar_name = "Redis"
    # start_rule = "root"
    # parser_path = Path(f"data/input/grammars/{domain}/{grammar_name}Parser.g4")
    # lexer_path = Path(f"data/input/grammars/{domain}/{grammar_name}Lexer.g4")
    # seeds_dir = SEEDS_DIR / domain
    # initial_grammar_paths = [parser_path, lexer_path]
    # skip_rules = ["SPACE"]
    # with_serializer = True

    domain = "SQL"
    grammar_name = "SQLSimplified"
    start_rule = "start"
    parser_path = Path(f"data/input/grammars/{domain}/{grammar_name}Parser.g4")
    lexer_path = Path(f"data/input/grammars/{domain}/{grammar_name}Lexer.g4")
    seeds_dir = SEEDS_DIR / domain
    initial_grammar_paths = [parser_path, lexer_path]
    skip_rules = ["Whitespace", "Newline"]
    with_serializer = True

    # domain = "JANUS"
    # grammar_name = "janus"
    # start_rule = "program"
    # parser_path = Path(f"data/input/grammars/{domain}/{grammar_name}.g4")
    # seeds_dir = SEEDS_DIR / domain
    # initial_grammar_paths = [parser_path]
    # skip_rules = ["WS"]
    # with_serializer = True

    # domain = "MDX"
    # grammar_name = "mdx"
    # start_rule = "mdx_statement"
    # parser_path = Path(f"data/input/grammars/{domain}/{grammar_name}.g4")
    # seeds_dir = SEEDS_DIR / domain
    # initial_grammar_paths = [parser_path]
    # skip_rules = ["WS"]
    # with_serializer = True

    num_inputs = 20
    max_length = 25

    build_model(
        domain,
        grammar_name,
        initial_grammar_paths,
        max_length,
        start_rule,
        num_inputs,
        skip_rules,
        with_serializer,
    )

    # mode = "with-generate"
    # sample_inputs(domain, mode, 200, max_length)

    # dataset_dir = DATASET_DIR / domain
    # antlr_output_dir = GEN_PARSER_DIR / domain
    # parser_final_file_path = GRAMMAR_FINAL_DIR / domain / f"{grammar_name}Parser.g4"
    # evaluate_PC(
    #     domain,
    #     dataset_dir,
    #     grammar_name,
    #     antlr_output_dir,
    #     parser_final_file_path,
    #     max_time=1500,
    # )
