from grammarinator_fuzzing.main import main as grammar_fuzz_main
from custom_generator_sql.main import main as custom_gen_sql_main
from GrammarRefactoring.main import refactor_grammar as grammar_refactoring_main
from GrammarRefactoring.refactor_grammar.checker import load_parser_lexer
from pathlib import Path
from cfg2pc.main import main_build_train_model, main_sampling

# === Global Path Variables ===
BASE_DIR = Path("data")
INTERMEDIATE_DIR = BASE_DIR / "intermediate"
OUTPUT_DIR = BASE_DIR / "output"
GENERATED_DIR = INTERMEDIATE_DIR / "generated"
GRAMMAR_DIR = INTERMEDIATE_DIR / "grammars"
GRAMMAR_REFACTORED_DIR = GRAMMAR_DIR
GRAMMAR_FINAL_DIR = GRAMMAR_DIR / "final"
GENERATOR_DIR = GENERATED_DIR / "generator"
POPULATION_DIR = GENERATED_DIR / "population"
GEN_PARSER_DIR = GENERATED_DIR / "parser"
FUZZ_OUTPUTS_DIR = INTERMEDIATE_DIR / "fuzz_outputs"
DATASET_DIR = INTERMEDIATE_DIR / "dataset"
SEEDS_DIR = BASE_DIR / "input" / "seeds"
MODEL_DIR = OUTPUT_DIR / "model"
SAMPLES_DIR = INTERMEDIATE_DIR / "samples"


def ensure_directories_exist():
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
    ]
    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)


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
    start_rule=None,
):
    # Create necessary directories
    ensure_directories_exist()

    print("-----Refactoring the grammar----\n")
    grammar = grammar_refactoring_main(
        domain,
        initial_grammar_paths,
        grammar_name,
        GRAMMAR_REFACTORED_DIR,
        GEN_PARSER_DIR,
        SEEDS_DIR,
        start_rule,
    )
    print("")

    # Fuzzing campaign
    print("-----Fuzzing Campaign-----")
    print("")
    grammar_fuzz_main(
        prefix_grammar=grammar_name,
        domain=domain,
        start_rule=start_rule,
        grammar_dir=GRAMMAR_FINAL_DIR,
        seeds_dir=SEEDS_DIR,
        generator_dir=GENERATOR_DIR,
        population_dir=POPULATION_DIR,
        gen_parser_dir=GEN_PARSER_DIR,
        fuzz_outputs_dir=FUZZ_OUTPUTS_DIR,
        dataset_dir=DATASET_DIR,
        num_inputs=10,
        first_time=True,
    )
    print("")

    max_length = 45
    nb_epochs = 10
    mode = "no-generate"

    # Build PC model
    print("-----Building the Probabilistic Circuit----")
    model_save_dir = MODEL_DIR / domain
    model_save_dir.mkdir(parents=True, exist_ok=True)

    model_save_path = model_save_dir / f"{domain}-{mode}.pt"

    trainingset_dir = DATASET_DIR / domain / mode / "train"
    antlr_output_dir = GEN_PARSER_DIR / domain
    _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)

    main_build_train_model(
        f"{GRAMMAR_FINAL_DIR}/{domain}/{grammar_name}Parser.g4",
        trainingset_dir,
        model_save_path,
        max_length,
        lexer_cls,
        nb_epochs,
    )


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


def sample_inputs(domain, mode, nb_inputs):
    model_save_path = MODEL_DIR / domain / f"{domain}-{mode}.pt"
    output_dir = SAMPLES_DIR / domain / mode
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"anonymized_inputs_{mode.replace('-','_')}.txt"
    main_sampling(model_save_path, nb_inputs, output_path)


def generate_inputs(model, domain, mode):
    sample_inputs(model)

    conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"

    input_file_name = f"anonymized_queries_{mode.replace('-','_')}.txt"
    query_input = INTERMEDIATE_DIR / "anonymized" / domain / input_file_name
    output_file_name = f"valid_inputs_{mode.replace('-','_')}.txt"
    output_dir = OUTPUT_DIR / domain
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / output_file_name

    success_rate = concretization(conninfo, query_input, output_path)

    custom_gen_sql_main(
        conninfo,
        query_input,
        output_path,
        max_queries=100,
        length_batch=20,
        dry_run=False,
    )

    return output_path, success_rate


if __name__ == "__main__":
    domain = "CSV"
    grammar_name = "CSV"
    start_rule = "csvFile"
    parser_path = Path("data/input/grammars/CSV/CSV.g4")
    seeds_dir = SEEDS_DIR / domain
    initial_grammar_paths = [parser_path]
    load_pc = None

    build_model(domain, grammar_name, initial_grammar_paths, start_rule)
    mode = "no-generate"
    sample_inputs(domain, mode, 200)
