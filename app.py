import gradio as gr

from inference import anonymize_original_input, ask_query, load_model_and_info
from main import get_literal_token_mapping, main_generate_inputs


def get_tokens(domain):
    literal_to_tokens = get_literal_token_mapping(domain)

    def custom_sort_key(item):
        if not item:
            return (2, "")
        elif item[0].isalpha():
            return (0, item)
        else:
            return (1, item)

    literals = list(literal_to_tokens.keys())
    literals = sorted(literals, key=custom_sort_key)
    return literals


def compute_probability(domain, query_type, inputs, mode):
    model, lit_map, lit_size, max_length = load_model_and_info(domain, mode)
    return ask_query(model, lit_map, lit_size, max_length, query_type, inputs)


def dispatch_probability_function(domain, question, lit1, lit2, lit3, pos, text, mode):
    fn = question_to_function[question]
    if not fn:
        return "Unsupported question selected."

    count = literal_count_by_question[question]
    has_pos = position_mapping[question]
    has_text = text_mapping.get(question, False)
    try:
        if has_text:
            return fn(domain, text, mode)
        if count == 1:
            if has_pos:
                return fn(domain, lit1, pos, mode)
            else:
                return fn(domain, lit1, mode)
        elif count == 2:
            if has_pos:
                return fn(domain, lit1, lit2, pos, mode)
            else:
                return fn(domain, lit1, lit2, mode)
        elif count == 3:
            if has_pos:
                return fn(domain, lit1, lit2, lit3, pos, mode)
            else:
                return fn(domain, lit1, lit2, lit3, mode)
        else:
            return "Unsupported number of literals."
    except Exception as e:
        return f"Error: {str(e)}"

def eval_mar1_all_tokens(domain, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    results = []
    valid_results = []

    for lit in literal_to_tokens.keys():
        try:
            result = prob_MAR1(domain, lit, mode)  # e.g. "LIT=0.1234 prob"
            results.append(result)
            valid_results.append(result)
        except Exception as e:
            results.append(f"Error processing {lit}: {str(e)}")
    
    results.sort(key=lambda x: float(x.split('=')[-1].strip().split()[0]))

    return "\n".join(results)

def eval_cond1_all_tokens(domain, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    results = []
    valid_results = []

    for lit1 in literal_to_tokens.keys():
        for lit2 in literal_to_tokens.keys():
            if lit1!=lit2:
                try:
                    result = prob_COND1(domain, lit1,lit2, mode) 
                    results.append(result)
                    valid_results.append(result)
                except Exception as e:
                    results.append(f"Error processing {lit1},{lit2}: {str(e)}")
    
    results.sort(key=lambda x: float(x.split('=')[-1].strip().split()[0]))

    return "\n".join(results)


def prob_MAR1(domain, lit, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    inputs = [token]
    query_type = "MAR1"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit})={prob:.4f}"


def prob_MAR2(domain, lit1, lit2, pos, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    tok1 = literal_to_tokens[lit1]
    tok2 = literal_to_tokens[lit2]
    inputs = ([tok1, tok2], pos)
    query_type = "MAR2"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P([{lit1},{lit2}])={prob:.4f} at position {pos}"


# def prob_MAR3(domain, lit1, lit2, mode):
#     literal_to_tokens = get_literal_token_mapping(domain)
#     token1 = literal_to_tokens[lit1]
#     token2 = literal_to_tokens[lit2]
#     inputs = [token1, token2]
#     query_type = "MAR2"
#     prob = compute_probability(domain, query_type, inputs, mode)
#     return f"P({lit})={prob:.4f}"


def prob_COND1(domain, lit1, lit2, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token1 = literal_to_tokens[lit1]
    token2 = literal_to_tokens[lit2]
    inputs = [token1, token2]
    query_type = "COND1"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit2}|{lit1})={prob:.4f}"


def prob_COND2(domain, lit1, lit2, pos, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token1 = literal_to_tokens[lit1]
    token2 = literal_to_tokens[lit2]
    inputs = ([token1, token2], pos)
    query_type = "COND2"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit2}|{lit1})={prob:.4f} at position {pos}"


def prob_COND3(domain, lit1, lit2, lit, pos, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token1 = literal_to_tokens[lit1]
    token2 = literal_to_tokens[lit2]
    tokens_list = [token1, token2]
    print("token list", tokens_list)
    tok = literal_to_tokens[lit]
    inputs = (tokens_list, tok, pos)
    print("inputs", inputs)
    query_type = "COND3"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit}|[{lit1},{lit2}])={prob:.4f} at position {pos}"


# def prob_MMAP1(domain, lit, mode):
#     literal_to_tokens = get_literal_token_mapping(domain)
#     token = literal_to_tokens[lit]
#     inputs = [token]
#     query_type = "MMAP1"
#     prob = compute_probability(domain, query_type, inputs, mode)
#     return f"P({lit})={prob:.4f}"


def prob_MMAP1(domain, lit, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    inputs = [token]
    query_type = "MMAP1"
    likely_token = compute_probability(domain, query_type, inputs, mode)
    return f"The most likely token to appear after {lit} is {likely_token}."


def prob_MMAP2(domain, lit, pos, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    inputs = (token, pos)
    query_type = "MMAP2"
    likely_token = compute_probability(domain, query_type, inputs, mode)
    return f"The most likely token to appear after {lit} is {likely_token}."


def prob_EVI(domain, input, mode):
    anonymized_input = anonymize_original_input(input, domain)
    inputs = (anonymized_input,)
    query_type = "EVI"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({input})={prob:.4f}"


def generate_inputs(domain, mode, num_inputs, sql_conn=None,literal_condition=None):
    literal_to_tokens = get_literal_token_mapping(domain)
    token_condition = [literal_to_tokens[lit] for lit in literal_condition] if literal_condition else None
    filename = main_generate_inputs(
        domain, mode, nb_concrete_inputs=num_inputs, conninfo=sql_conn,token_condition=token_condition
    )
    return filename


questions_by_type = {
    "Marginal": ["Marginal_1", "Marginal_2"],
    "Conditional": ["Conditional_1", "Conditional_2", "Conditional_3"],
    "Marginal Map": ["MarginalMap_1", "MarginalMap_2"],
    "Direct Evidence": ["DirectEvidence"],
}

question_description = {
    "Marginal_1": "P(Literal 1) ?",
    "Marginal_2": "P([Literal1,Literal2]), given that Literal 1 appears at position p ?",
    "Conditional_1": "P(Literal 2 | Literal 1), where Literal 2 appears anywhere after Literal 1 ?",
    "Conditional_2": "P(Literal 2 | Literal 1), where Literal 2 appears immediately after Literal 1 at position p ?",
    "Conditional_3": "P(Literal 3 | [Literal 1,Literal 2]) given that the sequence appears at position p ?",
    "MarginalMap_1": "What is the most likely token appearing anywhere after Literal 1 ?",
    "MarginalMap_2": "What is the most likely token appearing right after Literal 1 given it's at position p ?",
    "DirectEvidence": "What is the probability of seeing the structure of this query ?",
}

literal_count_by_question = {
    "Marginal_1": 1,
    "Marginal_2": 2,
    "Conditional_1": 2,
    "Conditional_2": 2,
    "Conditional_3": 3,
    "MarginalMap_1": 1,
    "MarginalMap_2": 1,
    "DirectEvidence": 1,
}

position_mapping = {
    "Marginal_1": False,
    "Marginal_2": True,
    "Conditional_1": False,
    "Conditional_2": True,
    "Conditional_3": True,
    "MarginalMap_1": False,
    "MarginalMap_2": True,
    "DirectEvidence": False,
}

text_mapping = {
    "DirectEvidence": True,
}

question_to_function = {
    "Marginal_1": prob_MAR1,
    "Marginal_2": prob_MAR2,
    "Conditional_1": prob_COND1,
    "Conditional_2": prob_COND2,
    "Conditional_3": prob_COND3,
    "MarginalMap_1": prob_MMAP1,
    "MarginalMap_2": prob_MMAP2,
    "DirectEvidence": prob_EVI,
}

max_length_mapping = {"SQL": 35, "B": 40, "REDIS": 10, "JANUS": 25}


with gr.Blocks() as demo:
    gr.Markdown("## ExplainFuzz")

    with gr.Row():
        domain = gr.Radio(
            ["SQL", "B", "REDIS", "JANUS","XML4"], label="Choose Domain", value="SQL"
        )

        mode = gr.Radio(
            ["with-generate", "no-generate"],
            value="no-generate",
            label="Mode:",
            interactive=True,
        )

    # Token list state to manage current token suggestions
    token_list = gr.State(get_tokens("SQL"))

    with gr.Tab("🤔 Inference Query"):
        with gr.Row():
            query_type = gr.Radio(
                choices=list(questions_by_type.keys()),
                label="Query Type",
                value="Marginal",
            )
            question = gr.Dropdown(
                choices=[
                    (question_description[q], q) for q in questions_by_type["Marginal"]
                ],
                label="Question",
            )

        with gr.Row():
            literal1 = gr.Dropdown(
                choices=get_tokens("SQL"), label="Literal 1", visible=True
            )
            literal2 = gr.Dropdown(
                choices=get_tokens("SQL"), label="Literal 2", visible=False
            )
            literal3 = gr.Dropdown(
                choices=get_tokens("SQL"), label="Literal 3", visible=False
            )
            position = gr.Slider(
                0, maximum=34, value=0, step=1, label="Position", visible=False
            )
            text = gr.Textbox(value=None, visible=False, label="Input")
            literals = [literal1, literal2, literal3]

        # Update function
        def update_question_choices(qtype):
            return gr.update(
                choices=[
                    (question_description[q], q) for q in questions_by_type[qtype]
                ],
                value=questions_by_type[qtype][0],
            )

        query_type.change(
            fn=update_question_choices, inputs=query_type, outputs=question
        )

        # When question changes, update literals
        def update_literal_dropdowns(q, domain):
            count = literal_count_by_question.get(q, 1)
            has_pos = position_mapping.get(q, False)
            max_length = max_length_mapping.get(domain, 10) - 1
            has_text = text_mapping.get(q, False)
            if has_text:
                return (
                    gr.update(visible=False, interactive=False),
                    gr.update(visible=False, interactive=False),
                    gr.update(visible=False, interactive=False),
                    gr.update(visible=False, interactive=False),
                    gr.update(visible=True, interactive=True),
                )
            return (
                gr.update(visible=(count >= 1), interactive=(count >= 1)),
                gr.update(visible=(count >= 2), interactive=(count >= 2)),
                gr.update(visible=(count >= 3), interactive=(count >= 3)),
                gr.update(visible=has_pos, interactive=has_pos, maximum=max_length),
                gr.update(visible=has_text, interactive=has_text),
            )

        question.change(
            fn=update_literal_dropdowns,
            inputs=[question, domain],
            outputs=[literal1, literal2, literal3, position, text],
        )

        prob_button = gr.Button("Get Probability")
        prob_output = gr.Label()

        prob_button.click(
            fn=dispatch_probability_function,
            inputs=[
                domain,
                question,
                literal1,
                literal2,
                literal3,
                position,
                text,
                mode,
            ],
            outputs=prob_output,
        )

        # with gr.Row():
        #     gr.Markdown("### Or evaluate MAR1 for all tokens")
        #     eval_all_btn = gr.Button("Evaluate All")
        #     eval_all_output = gr.Textbox(label="Results")
        #     eval_all_btn.click(
        #         fn=eval_mar1_all_tokens,
        #         inputs=[domain, mode],
        #         outputs=eval_all_output,
        #     )
        # with gr.Row():
        #     gr.Markdown("### Or evaluate COND1 for all token pairs")
        #     eval_all_cond1_btn = gr.Button("Evaluate All COND1")
        #     eval_all_cond1_output = gr.Textbox(label="Results")
        #     eval_all_cond1_btn.click(
        #         fn=eval_cond1_all_tokens,
        #         inputs=[domain, mode],
        #         outputs=eval_all_cond1_output,
        #     )

    with gr.Tab("🧬 Input Generator"):
        sql_conn = gr.Textbox(
            label="PostgreSQL Connection String",
            placeholder="dbname=? user=? password=? host=? port=?",
        )
        num_inputs = gr.Slider(10, 1000, value=500, step=10, label="Number of Inputs")
        
        # --- OPTIONAL TOKEN SEQUENCE UI ---
        use_token_sequence = gr.Checkbox(label="Condition the generation on a sequence of tokens?", value=False)

        MAX_LEN = 10  # you can set the maximum allowed
        seq_length = gr.Slider(1, MAX_LEN, value=1, step=1, label="Sequence Length", visible=False)

        token_dropdowns = [
            gr.Dropdown(get_tokens("SQL"), label=f"Token {i+1}", visible=False)
            for i in range(MAX_LEN)
        ]

        generate_btn = gr.Button("Generate")
        output_file = gr.File()
        generation_status = gr.Label()

        def toggle_sequence_fields(use_seq):
            updates = []

            # Show length chooser only if checkbox checked
            updates.append(gr.update(visible=use_seq))

            
            updates.append(gr.update(visible=True))
            for _ in range(1,MAX_LEN):
                updates.append(gr.update(visible=False))

            return updates

        use_token_sequence.change(
            fn=toggle_sequence_fields,
            inputs=use_token_sequence,
            outputs=[seq_length] + token_dropdowns,
        )

        def update_token_dropdowns(length):
            updates = []
            for i in range(MAX_LEN):
                if i < length:
                    updates.append(gr.update(visible=True))
                else:
                    updates.append(gr.update(visible=False))
            return updates

        seq_length.change(
            fn=update_token_dropdowns,
            inputs=seq_length,
            outputs=token_dropdowns,
        )

        def run_generation(domain, mode, sql_conn, num_inputs, use_seq, seq_length, *tokens):
            token_condition = None
            if use_seq:
                token_condition = list(tokens[:seq_length])

            generation_status = f"Generating {num_inputs} inputs for {domain}..."

            # Pass token_condition as an extra argument
            zip_file = generate_inputs(domain, mode, int(num_inputs), sql_conn, token_condition)

            return zip_file, f"Done! Download the generated inputs."

        generate_btn.click(
            fn=run_generation,
            inputs=[domain, mode, sql_conn, num_inputs,
                    use_token_sequence, seq_length] + token_dropdowns,
            outputs=[output_file, generation_status],
        )

        def update_all_dropdowns(domain):
            tokens = get_tokens(domain)

            updates = []

            # Update old literal dropdowns
            for _ in literals:
                updates.append(gr.update(choices=tokens, value=None, interactive=True))

            # Update token sequence dropdowns
            for _ in token_dropdowns:
                updates.append(gr.update(choices=tokens, value=None, interactive=True))

            updates.append(tokens)

            return updates

        domain.change(
            fn=update_all_dropdowns,
            inputs=domain,
            outputs=literals + token_dropdowns + [token_list],
        )

        
if __name__ == "__main__":
    demo.launch()
