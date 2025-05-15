from grammarinator_fuzzing.main import main as grammar_fuzz_main
from custom_generator_sql.main import main as custom_gen_sql_main
from GrammarRefactoring.main import refactor_grammar as grammar_refactoring_main
import os
import torch
from pathlib import Path
import argparse
from cfg2pc.grammar import parse_grammar
from cfg2pc.circuit import semi_naive_circuit
from cfg2pc.dataset import get_tensorized_dataset_from_folder
from cfg2pc.main import train

def build_pc(grammar_path, max_length):
    res = {}
    grammar = parse_grammar(grammar_path)
    circuit, lit_map = semi_naive_circuit(grammar, max_length, res)
    model = circuit.to_torch_module(semiring="log", probabilistic=True)

    return model, lit_map, res["circuit_size"]

def fuzzing_campaign(prefix_grammar, domain, start_rule):
    grammar_fuzz_main(
        prefix_grammar=prefix_grammar,
        domain=domain,
        start_rule=start_rule,
        num_inputs=10,
        first_time=True,
    )

def refactoring_grammar(domain, initial_grammar_path, grammar_name, grammar_refactored_dir,parser_generated_dir,start_rule):
    grammar,parser_path,lexer_path = grammar_refactoring_main(
        domain, initial_grammar_path, grammar_name, grammar_refactored_dir,parser_generated_dir, start_rule
    )
    return grammar,parser_path,lexer_path 

def train_pc(model, dataset, epochs):
    res = {}
    train(dataset, model, epochs, res)
    return model, res["last-training-loss"]

def build_model(domain,grammar_name,initial_grammar_paths,seeds_dir,load_pc,start_rule=None):
    # Refactoring the grammar
    
    grammar_refactored_dir = Path("data/intermediate/grammars/")
    grammar_final_dir = Path("data/intermediate/grammars/final/")
    generator_dir = Path("data/intermediate/generated/generator/")
    population_dir = Path("data/intermediate/generated/population/")
    gen_parser_dir = Path("data/intermediate/generated/parser/")
    fuzz_outputs_dir = Path("data/intermediate/fuzz_outputs/")
    dataset_dir = Path("data/intermediate/dataset/")
    seeds_dir = Path("data/input/seeds/")
    models_dir = Path("out/models/")
    models_dir.mkdir(parents=True, exist_ok=True)

    for directory in [grammar_refactored_dir,grammar_final_dir,generator_dir, population_dir, gen_parser_dir, fuzz_outputs_dir, dataset_dir,seeds_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    print("-----Refactoring the grammar----")
    print("")
    grammar = grammar_refactoring_main(
        domain, initial_grammar_paths, grammar_name, grammar_refactored_dir,gen_parser_dir, seeds_dir,start_rule
    )
    print("")


    # Fuzzing campaign
    print("-----Fuzzing Campaign-----")
    print("")
    grammar_fuzz_main(
        prefix_grammar=grammar_name,
        domain=domain,
        start_rule=start_rule,
        grammar_dir = grammar_final_dir,
        seeds_dir = seeds_dir,
        generator_dir = generator_dir,
        population_dir = population_dir,
        gen_parser_dir = gen_parser_dir,
        fuzz_outputs_dir = fuzz_outputs_dir,
        dataset_dir = dataset_dir,
        num_inputs=10,
        first_time=True,
    )
    print("")

    max_length = 20
    nb_epochs = 10

    # CFG to PC
    if load_pc == None:
        print("-----Building the Probabilistic Circuit----")
        save_model_dir = Path("data/intermediate/model")
        save_model_dir.mkdir(parents=True, exist_ok=True)
        mode = "no-generate"
        #model = train_pc(grammar,grammar_name,domain,start_rule,mode,save_model_dir)
        model, lit_map, size = build_pc(f"{grammar_final_dir}/{grammar_name}/{grammar_name}Parser.g4", max_length)
        model.size = size
        # train here
        train_path = f"{dataset_dir}/{domain}/no-generate/train"
        # this is not the right function to load datasets
        #train = get_tensorized_dataset_from_folder(train_path, grammar, max_length, lit_map)
        print(f"-> Loaded training dataset from {train_path} of length {len(train)}")
        torch.save(model, f"{models_dir}/{domain}_{max_length}.pt")
        model, loss = train_pc(model, train, nb_epochs)
        print(f"-> Trained Circuit over {nb_epochs} epochs with loss={loss}")
    else:
        model = torch.load(load_pc, weights_only=False)
        print(f"-> Circuit loaded with {model.size} nodes")

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

    domain = "XML"
    grammar_name = "XML"
    start_rule = "document"
    parser_path = "data/input/grammars/XML/XMLParser.g4"
    lexer_path = "data/input/grammars/XML/XMLLexer.g4"
    seeds_dir = "data/input/seeds/XML/"
    grammar_dir = "data/intermediate/grammars/"
    load_pc = None
    initial_grammar_paths =[parser_path,lexer_path]


    build_model(domain,grammar_name,initial_grammar_paths,seeds_dir,load_pc,start_rule)
