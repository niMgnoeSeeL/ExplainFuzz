from grammarinator_fuzzing.main import main as grammar_fuzz_main

def fuzzing_campaign(prefix_grammar,domain,start_rule):
    grammar_fuzz_main(
        prefix_grammar=prefix_grammar,
        domain=domain,
        start_rule=start_rule,
        num_inputs=10,
        first_time=False
    )