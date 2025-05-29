from antlr4 import InputStream
from GrammarRefactoring.refactor_grammar.GrammarVisitor import parse_grammar_antlr
from GrammarRefactoring.refactor_grammar.LexerRuleExtractor import (
    get_token_to_literal_mapping,
    get_literal_to_token_mapping,
)
from grammarinator_fuzzing.main import main as grammarinator_fuzz_main
from custom_generator_sql.main import main as custom_gen_sql_main
from GrammarRefactoring.main import (
    refactor_grammar as grammar_refactoring_main,
)
from GrammarRefactoring.refactor_grammar.checker import load_parser_lexer
from pathlib import Path

from cfg2pc.main import main_build_train_model, main_sampling
import json

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


def build_model(
    domain,
    grammar_name,
    initial_grammar_paths,
    max_length,
    start_rule=None,
    num_inputs=10,
    skip_rules=[],
    with_serializer=False,
    depth=20,
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

    # ============================================================
    #                 GRAMMAR REFACTORING
    # ------------------------------------------------------------
    # This block handles grammar preprocessing to ensure
    # compatibility with the PC compiler. It refactors ANTLR4
    # grammars (Parser.g4, Lexer.g4) by simplifying rules,
    # removing quantifiers (*, +, ?), and converting the grammar
    # to a form similar to Chomsky Normal Form (CNF).
    #
    # The algorithm propagates and eliminates nullable rules,
    # ensuring all productions meet structural constraints
    # required for circuit construction.
    # ============================================================

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

    # grammar = grammar_refactoring_main(
    #     initial_grammar_paths,
    #     grammar_name,
    #     intermediate_dir,
    #     refactored_dir,
    #     final_dir,
    #     antlr_output_dir,
    #     seeds_dir,
    #     start_rule,
    # )

    parser_final_file_path = final_dir / f"{grammar_name}Parser.g4"
    print("")

    # ============================================================
    #                    FUZZING CAMPAIGN
    # ------------------------------------------------------------
    # This section launches the fuzzing campaign to generate a
    # large number of test inputs. Starting from a small seed set
    # (e.g., ~5 examples), the system uses Grammarinator along
    # with the refactored lexer and parser to generate 10,000 new
    # inputs that conform to the grammar.
    # ============================================================

    print("-----Fuzzing Campaign-----")
    print("")

    generator_dir = GENERATOR_DIR / domain
    population_dir = POPULATION_DIR / domain
    fuzz_outputs_dir = FUZZ_OUTPUTS_DIR / domain
    dataset_dir = DATASET_DIR / domain
    fuzzing_dirs = [generator_dir, population_dir, fuzz_outputs_dir, dataset_dir]
    ensure_directories_exist(fuzzing_dirs)

    # grammarinator_fuzz_main(
    #     prefix_grammar=grammar_name,
    #     start_rule=start_rule,
    #     grammar_dir=final_dir,
    #     seeds_dir=seeds_dir,
    #     generator_dir=generator_dir,
    #     population_dir=population_dir,
    #     gen_parser_dir=antlr_output_dir,
    #     fuzz_outputs_dir=fuzz_outputs_dir,
    #     dataset_dir=dataset_dir,
    #     num_inputs=num_inputs,
    #     first_time=True,
    #     with_serializer=with_serializer,
    #     depth=depth,
    # )
    print("")

    # ============================================================
    #                 PC COMPILATION + TRAINING
    # ------------------------------------------------------------
    # This section handles the transformation of the grammar into
    # a Probabilistic Circuit (PC). Once the grammar is formatted
    # correctly, the system compiles it using structural analysis
    # of the rules defined in the Parser.g4 file.
    # ============================================================

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

        main_build_train_model(
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


# ============================================================
#                      PC INFERENCE
# ------------------------------------------------------------
# This section enables querying the Probabilistic Circuit (PC)
# to analyze and understand the structure of possible inputs.
# Beyond sampling, it supports inference queries that estimate
# the likelihood of specific grammatical patterns or constructs
# (e.g., what is the probability that a WHERE clause appears
# in SQL a query).
# ============================================================


def inference(domain, max_length, grammar_name, type_of_question):
    "Make inference"
    return


# ====================================================================
#                          PC Sampling
# --------------------------------------------------------------------
# This function enables sampling inputs from the PC according to the
# distribution of the initial inputs.
# =====================================================================


def get_domain_config(domain):
    config_file_path = Path("domains_config.json").resolve()
    domains_config = load_domains_config(config_file_path)
    domain_config = domains_config[domain]
    return domain_config


def sample_inputs(domain, mode, nb_inputs):
    domain_config = get_domain_config(domain)
    max_length = domain_config["max_length"]

    model_save_path = MODEL_DIR / domain / f"{domain}-{mode}-{max_length}.pt"
    output_dir = SAMPLES_DIR / domain / mode
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"anonymized_inputs_{mode.replace('-','_')}.txt"
    main_sampling(model_save_path, nb_inputs, output_path)


# ====================================================================
#                          CONCRETIZATION
# --------------------------------------------------------------------
# This section is responsible for translating anonymized inputs
# sampled from the PC to concrete inputs.
# For the SQL domain it uses a custom generator to convert the queries
# into executable queries. For the other domain, we map the symbolic
# tokens to their actual string literals when it's a 1 to 1 mapping.
# =====================================================================


def get_literal_token_mapping(domain: str):
    """Get the literal mapping from the lexer file"""
    domain_config = get_domain_config(domain)
    lexer_path = (
        GRAMMAR_DIR / "final" / domain / f"{domain_config['grammar_name']}Lexer.g4"
    )
    parser_path = (
        GRAMMAR_DIR / "final" / domain / f"{domain_config['grammar_name']}Parser.g4"
    )
    literal_token_mapping = get_literal_to_token_mapping(lexer_path)

    _, terminals = parse_grammar_antlr(str(parser_path))
    for terminal in terminals:
        if terminal not in literal_token_mapping.values():
            literal_token_mapping[terminal] = terminal
    return literal_token_mapping


def deanonymize_samples(domain, samples_path, output_path):
    with open(samples_path, "r") as file:
        lines = file.readlines()
    samples = [q.strip().split() for q in lines]

    literal_map_reversed = get_literal_token_mapping(domain)
    literal_map = {}
    for key, value in literal_map_reversed.items():
        literal_map[value] = key
    literal_map["EOF"] = ""
    for rule, value in literal_map.items():
        if value.startswith("'") and value.endswith("'"):
            literal_map[rule] = value[1:-1]

    partial_concrete_inputs = []
    for sample in samples:
        partial_concrete_inputs += [[literal_map.get(t, t.lower()) for t in sample]]

    with open(output_path, "w") as file:
        for input in partial_concrete_inputs:
            file.write(" ".join(input) + "\n")


def concretization(domain, mode, conninfo, nb_concrete_inputs):
    output_dir = OUTPUT_DIR / "inputs" / domain
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"inputs_{mode.replace('-','_')}.txt"

    input_file_name = f"anonymized_inputs_{mode.replace('-','_')}.txt"
    samples_path = SAMPLES_DIR / domain / mode / input_file_name

    if domain == "SQL":
        conninfo = (
            "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"
        )
        custom_gen_sql_main(
            conninfo,
            query_input=str(samples_path),
            output_path=output_path,
            max_queries=nb_concrete_inputs,
            length_batch=20,
            dry_run=False,
        )
    else:
        deanonymize_samples(domain, samples_path, output_path)
    return str(output_path)


def main_generate_inputs(domain, mode, nb_concrete_inputs=200, conninfo=None):
    if domain == "SQL":
        nb_sample_inputs = nb_concrete_inputs // 20 + 1
    else:
        nb_sample_inputs = nb_concrete_inputs

    sample_inputs(domain, mode, nb_sample_inputs)
    output_path = concretization(domain, mode, conninfo, nb_concrete_inputs)
    return output_path


def load_domains_config(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


if __name__ == "__main__":

    config_file_path = "domains_config.json"
    domains_config = load_domains_config(config_file_path)

    domain = "SQL"
    domain_config = domains_config[domain]

    get_literal_token_mapping2("SQL")

    num_inputs = 10000
    # mode = "no-generate"
    # main_generate_inputs(domain, mode, domain_config["max_length"])

    # build_model(
    #     domain,
    #     grammar_name=domain_config["grammar_name"],
    #     initial_grammar_paths=domain_config["initial_grammar_paths"],
    #     max_length=domain_config["max_length"],
    #     start_rule=domain_config["start_rule"],
    #     num_inputs=num_inputs,
    #     skip_rules=domain_config["skip_rules"],
    #     with_serializer=domain_config["with_serializer"],
    #     depth=domain_config["depth"],
    # )

    # generate_anonymized_dataset(
    #     domain,
    #     grammar_name=domain_config["grammar_name"],
    #     start_rule=domain_config["start_rule"],
    #     skip_rules=domain_config["skip_rules"],
    #     output_dir=Path("anonymized_dataset/SQL/"),
    # )

    # for mode in ["no-generate", "with-generate"]:
    #     sample_inputs(domain, mode, 500)

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
