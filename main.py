from grammarinator_fuzzing.main import main as grammar_fuzz_main
from custom_generator_sql.main import main as custom_gen_sql_main
import os
from pathlib import Path
import argparse

def fuzzing_campaign(prefix_grammar, domain, start_rule):
    grammar_fuzz_main(
        prefix_grammar=prefix_grammar,
        domain=domain,
        start_rule=start_rule,
        num_inputs=10,
        first_time=True,
    )

def refactoring_grammar(initial_grammar,grammar_refactored_dir):
    # Creates a Lexer and Parser
    start_rule = ""
    prefix_grammar = ""
    lexer_path = ""
    parser_path = ""
    return prefix_grammar,start_rule,lexer_path,parser_path

def train_pc(prefix_grammar,domain,start_rule,mode):
    model = ""
    return model

def build_model(domain,initial_grammar,seeds_dir,start_rule=None):
    # Refactoring the grammar
    initial_grammar = "data/input/initial_grammars/"
    grammar_refactored_dir = "data/input/grammars/"
    prefix_grammar,start_rule = refactoring_grammar(initial_grammar,grammar_refactored_dir)

    # Fuzzing campaign
    seeds_dir = "data/input/seeds/"

    generator_dir = Path("data/intermediate/generated/generator/")
    population_dir = Path("data/intermediate/generated/population/")
    gen_parser_dir = Path("data/intermediate/generated/parser/")
    fuzz_outputs_dir = Path("data/intermediate/fuzz_outputs/")
    dataset_dir = Path("data/intermediate/dataset/")

    for directory in [generator_dir, population_dir, gen_parser_dir, fuzz_outputs_dir, dataset_dir]:
        directory.mkdir(parents=True, exist_ok=True)
     
    grammar_fuzz_main(
        prefix_grammar=prefix_grammar,
        domain=domain,
        start_rule=start_rule,
        grammar_dir = grammar_refactored_dir,
        seeds_dir = seeds_dir,
        generator_dir = generator_dir,
        population_dir = population_dir,
        gen_parser_dir = gen_parser_dir,
        fuzz_outputs_dir = fuzz_outputs_dir,
        dataset_dir = dataset_dir,
        num_inputs=10,
        first_time=True,
    )

    # CFG to PC
    save_model_dir = Path("data/intermediate/model")
    save_model_dir.mkdir(parents=True, exist_ok=True)
    
    model = train_pc(prefix_grammar,domain,start_rule,mode,save_model_dir)

    return model 

def get_pre_trained_model(domain,mode,save_model_dir):
    # Load the model
    model = ""
    return model  

def inference(model):
    "Make inference"
    return 

def concretization(conninfo, anonymized_queries,output_path):
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

def sample_inputs(model):
    return 

def generate_inputs(model,domain,mode):
    # sample anonymized inputs from the PC
    sample_inputs(model)

    # Generation real inputs
    conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432" #only for SQL

    input_file_name = f"anonymized_queries_{mode.replace('-','_')}.txt"
    query_input = os.path.join("data/intermediate/anonymized/",domain,input_file_name)
    output_file_name = f"valid_inputs_{mode.replace('-','_')}.txt" 
    output_dir = Path(os.path.join("data/output/",domain))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = os.path.join(output_dir,output_file_name)
    success_rate = concretization(conninfo, query_input,output_path)
    
    custom_gen_sql_main(
        conninfo,
        query_input,
        output_path,
        max_queries=100,
        length_batch=20,
        dry_run=False,
    )

    return output_path,success_rate



if __name__=="__main__":
    # Test for SQL
    prefix_grammar = "SQLSimplified"
    domain = "SQL"
    start_rule = "start"
    fuzzing_campaign(prefix_grammar, domain, start_rule)

    # Generation inputs
    conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"
    mode = "no-generate"
    input_file_name = f"anonymized_queries_{mode.replace('-','_')}.txt"
    query_input = os.path.join("data/intermediate/anonymized/",domain,input_file_name)
    output_file_name = f"valid_inputs_{mode.replace('-','_')}.txt" 
    output_dir = Path(os.path.join("data/output/",domain))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = os.path.join(output_dir,output_file_name)
    success_rate = concretization(conninfo, query_input,output_path)
    print("The success rate is",success_rate)

  
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix_grammar", type=str)
    parser.add_argument("--domain", type=str)
    parser.add_argument("--start_rule", type=str)
    args = parser.parse_args()
    # main(args.prefix_grammar, args.domain, args.start_rule)
