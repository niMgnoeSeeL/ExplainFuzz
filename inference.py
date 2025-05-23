from GrammarRefactoring.refactor_grammar.LiteralExractor import (
    extract_existing_literals,
)
from cfg2pc.query import marginal_query, marginal_query_cond
from main import GRAMMAR_DIR, MODEL_DIR, load_domains_config
import torch
from pathlib import Path


def get_literal_token_mapping(domain: str):
    """Get the literal mapping from the lexer file"""
    config_file_path = Path("domains_config.json").resolve()
    domains_config = load_domains_config(config_file_path)
    domain_config = domains_config[domain]
    lexer_path = (
        GRAMMAR_DIR / "final" / domain / f"{domain_config['grammar_name']}Lexer.g4"
    )
    literal_token_mapping = extract_existing_literals(lexer_path)
    return literal_token_mapping


def load_model_and_info(domain: str, mode: str):
    config_file_path = Path("domains_config.json").resolve()
    domains_config = load_domains_config(config_file_path)
    domain_config = domains_config[domain]
    max_length = domain_config["max_length"]
    model_save_path = MODEL_DIR / domain / f"{domain}-{mode}-{max_length}.pt"
    model = torch.load(model_save_path, weights_only=False)
    model.eval()
    lit_map = model.lit_map
    lit_size = max(l for l in lit_map.values()) + 1
    return model, lit_map, lit_size, max_length


def ask_query(
    model, lit_map: dict, lit_size: int, max_length: int, query_type: str, inputs: list
):
    match query_type:
        case "MAR1":
            tok = inputs[0]
            prob = abs(marginal_query(model, tok, lit_map, lit_size, max_length))
            return prob
        case "MAR2":
            # retrive the inputs and call the correct function
            pass
        case "MAR3":
            # retrive the inputs and call the correct function
            pass
        case "COND1":
            tok = inputs[0]
            tok2 = inputs[1]
            prob = abs(
                marginal_query_cond(model, tok, tok2, lit_map, lit_size, max_length)
            )
            return prob
        case "COND2":
            # retrive the inputs and call the correct function
            pass
        case "COND3":
            # retrive the inputs and call the correct function
            pass
        case "EVI":
            # retrive the inputs and call the correct function
            pass
        case "MAP":
            # retrive the inputs and call the correct function
            pass
        case "MMAP":
            # retrive the inputs and call the correct function
            pass


if __name__ == "__main__":
    domain = "SQL"
    grammar_name = "SQLSimplified"
    literal_token_mapping = get_literal_token_mapping(domain, grammar_name)
    # print(literal_token_mapping)

    # mode = "no-generate"
    # max_length = 10
    # model, lit_map, lit_size = load_model_and_info(domain, mode, max_length)
