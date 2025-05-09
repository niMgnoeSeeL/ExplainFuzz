from grammarinator_fuzzing.main import main as grammar_fuzz_main
from custom_generator_sql.generator import main as custom_gen_sql_main

def fuzzing_campaign(prefix_grammar,domain,start_rule):
    grammar_fuzz_main(
        prefix_grammar=prefix_grammar,
        domain=domain,
        start_rule=start_rule,
        num_inputs=10,
        first_time=False
    )

def concretization(conninfo,anonymized_queries,lexer_file_path):
    max_queries=1000
    length_batch=20
    custom_gen_sql_main(conninfo,anonymized_queries,max_queries,length_batch,lexer_file_path,dry_run=False)