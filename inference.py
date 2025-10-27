from GrammarRefactoring.refactor_grammar.checker import load_parser_lexer
from cfg2pc.dataset import anonymize_one_input
from cfg2pc.query import (
    marginal_query,
    marginal_query_cond,
    evi_query,
    marginal_sequence_query,
    marginal_query_contiguous_cond,
    sequential_query_contiguous_cond,
    marginal_map_query,
    marginal_map_query2,
)
from main import (
    GEN_PARSER_DIR,
    MODEL_DIR,
    get_domain_config,
    get_literal_token_mapping,
    load_domains_config,
)
import torch
from pathlib import Path


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
    model, lit_map: dict, lit_size: int, max_length: int, query_type: str, inputs: tuple
):
    match query_type:
        case "MAR1":
            tok = inputs[0]
            prob = abs(marginal_query(model, tok, lit_map, lit_size, max_length))
            return prob
        case "MAR2":
            """represent input as ([token1,...],pos)"""
            sequence = inputs[0]
            pos = inputs[1]
            prob = abs(marginal_sequence_query(model, sequence, lit_map, lit_size, pos))
            return prob
        case "COND1":
            """represent input as ([token1, token1])"""
            tok = inputs[0]
            tok2 = inputs[1]
            prob = abs(
                marginal_query_cond(model, tok, tok2, lit_map, lit_size, max_length)
            )
            return prob
        case "COND2":
            """represent input as ([token1, token1], pos)"""
            tok = inputs[0][0]
            tok2 = inputs[0][1]
            pos = inputs[1]
            prob = abs(
                marginal_query_contiguous_cond(model, tok, tok2, lit_map, lit_size, pos)
            )
            return prob
        case "COND3":
            """represent input as ([token1, token2...],tok, pos)"""
            sequence, tok, pos = inputs
            print(sequence, tok, pos)
            prob = abs(
                sequential_query_contiguous_cond(
                    model, tok, sequence, lit_map, lit_size, pos
                )
            )
            return prob
        case "EVI":
            seq = inputs[0]
            print(seq)
            new_seq = seq + ["PAD"] * (max_length - len(seq))
            print(new_seq, len(new_seq))
            prob = abs(evi_query(model, new_seq, lit_map, lit_size))
            return prob
        case "MMAP1":
            tok = inputs[0]
            most_probable_token = marginal_map_query(
                model, tok, lit_map, lit_size, max_length
            )
            return most_probable_token
        case "MMAP2":
            """represent input as (tok,pos)"""
            tok = inputs[0]
            pos = inputs[1]
            most_probable_token = marginal_map_query2(
                model, tok, lit_map, lit_size, pos
            )
            return most_probable_token


def anonymize_original_input(input, domain):
    domain_config = get_domain_config(domain)
    skip_rules = domain_config["skip_rules"]
    grammar_name = domain_config["grammar_name"]
    antlr_output_dir = GEN_PARSER_DIR / domain
    _, lexer_cls = load_parser_lexer(grammar_name, antlr_output_dir)
    anonymized_input = anonymize_one_input(input, lexer_cls, skip_rules)
    return anonymized_input + ["EOF"]


def compute_probability(domain, query_type, inputs, mode):
    model, lit_map, lit_size, max_length = load_model_and_info(domain, mode)
    return ask_query(model, lit_map, lit_size, max_length, query_type, inputs)


if __name__ == "__main__":
    domain = "SQL"
    grammar_name = "SQLSimplified"
    literal_token_mapping = get_literal_token_mapping(domain)
    # print(literal_token_mapping)

    # mode = "no-generate"
    # max_length = 10
    # model, lit_map, lit_size = load_model_and_info(domain, mode, max_length)
