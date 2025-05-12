from grammarinator_fuzzing.main import main as grammar_fuzz_main

# from custom_generator_sql.generator import main as custom_gen_sql_main


def fuzzing_campaign(prefix_grammar, domain, start_rule):
    grammar_fuzz_main(
        prefix_grammar=prefix_grammar,
        domain=domain,
        start_rule=start_rule,
        num_inputs=10,
        first_time=True,
    )

if __name__=="__main__":
    # Test for SQL
    prefix_grammar = "SQLSimplified"
    domain = "SQL"
    start_rule = "start"

    fuzzing_campaign(prefix_grammar, domain, start_rule)


# def concretization(conninfo, anonymized_queries, lexer_file_path):
#     max_queries = 1000
#     length_batch = 20
#     custom_gen_sql_main(
#         conninfo,
#         anonymized_queries,
#         max_queries,
#         length_batch,
#         lexer_file_path,
#         dry_run=False,
#     )


# conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"
# anonymized_queries_file = "queries/anonymized/anonymized_queries_no_generate.txt"
# lexer_file_path = "grammars/SQL/SQLSimplifiedLexer.g4"

# # main.py


# # Paths
# grammar_input_path = "data/input/original_grammar.g4"
# refactored_parser_path = "data/intermediate/Parser.g4"
# refactored_lexer_path = "data/intermediate/Lexer.g4"
# seeds_path = "data/input/seeds/"
# training_data_path = "data/intermediate/train.json"
# testing_data_path = "data/intermediate/test.json"
# parser_py_path = "data/intermediate/Parser.py"
# lexer_py_path = "data/intermediate/Lexer.py"
# anonymized_inputs_path = "data/intermediate/anonymized_inputs.json"
# final_output_path = "data/output/generated_inputs.txt"

# Step 1: Grammar refactoring
# refactor_grammar(grammar_input_path, refactored_parser_path, refactored_lexer_path)

# Step 2: Fuzzing
# run_fuzzing(refactored_parser_path, refactored_lexer_path, seeds_path,
#             training_data_path, testing_data_path,
#             parser_py_path, lexer_py_path)

# Step 3: CFG to PC conversion
# convert_to_pc(training_data_path, testing_data_path,
#               refactored_parser_path, refactored_lexer_path,
#               anonymized_inputs_path)

# Step 4: Generation
# generate_inputs(anonymized_inputs_path, refactored_lexer_path,
#                 parser_py_path, lexer_py_path, final_output_path)
