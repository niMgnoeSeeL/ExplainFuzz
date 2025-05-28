from pathlib import Path
import gradio as gr

from inference import ask_query, load_model_and_info
from main import get_literal_token_mapping, main_generate_inputs

""""This is a dummy FE for now"""


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


def dispatch_probability_function(domain, question, lit1, lit2, lit3, pos, mode):
    fn = question_to_function[question]
    if not fn:
        return "Unsupported question selected."

    count = literal_count_by_question[question]
    has_pos = position_mapping[question]
    try:
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


# TODO : Prepare all the functions for each type of query
def prob_MAR1(domain, lit, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    print(f"Token for {lit}: {token}")
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


def prob_MMAP(domain, lit, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    inputs = [token]
    query_type = "MMAP"
    likely_token = compute_probability(domain, query_type, inputs, mode)
    return f"The most likely token to appear after {lit} is {likely_token}."


def prob_EVI(domain, lit, mode):
    # TODO : modify that
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    inputs = [token]
    query_type = "EVI"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit})={prob:.4f}"


def generate_inputs(domain, mode, num_inputs, sql_conn=None):
    filename = main_generate_inputs(
        domain, mode, nb_concrete_inputs=num_inputs, conninfo=sql_conn
    )
    return filename


questions_by_type = {
    "Marginal": ["Marginal_1", "Marginal_2"],
    "Conditional": ["Conditional_1", "Conditional_2", "Conditional_3"],
    "Marginal Map": ["MarginalMap"],
    "Direct Evidence": ["DirectEvidence"],
}

question_description = {
    "Marginal_1": "P(Literal 1) ?",
    "Marginal_2": "P([Literal1,Literal2]), given that Literal 1 appears at position p ?",
    "Conditional_1": "P(Literal 2 | Literal 1), where Literal 2 appears anywhere after Literal 1 ?",
    "Conditional_2": "P(Literal 2 | Literal 1), where Literal 2 appears immediately after Literal 1 at position p ?",
    "Conditional_3": "P(Literal 3 | [Literal 1,Literal 2]) given that the sequence appears at position p ?",
    "MarginalMap": "What is the most likely token appearing anywhere after Literal 1 ?",
    "DirectEvidence": "What is the probability of seeing the structure of this query ?",
}

literal_count_by_question = {
    "Marginal_1": 1,
    "Marginal_2": 2,
    "Conditional_1": 2,
    "Conditional_2": 2,
    "Conditional_3": 3,
    "MarginalMap": 1,
    "DirectEvidence": 1,
}

position_mapping = {
    "Marginal_1": False,
    "Marginal_2": True,
    "Conditional_1": False,
    "Conditional_2": True,
    "Conditional_3": True,
    "MarginalMap": False,
    "DirectEvidence": False,
}

question_to_function = {
    "Marginal_1": prob_MAR1,
    "Marginal_2": prob_MAR2,
    "Conditional_1": prob_COND1,
    "Conditional_2": prob_COND2,
    "Conditional_3": prob_COND3,
    "MarginalMap": prob_MMAP,
    "DirectEvidence": prob_EVI,
}

max_length_mapping = {"SQL": 35, "B": 40, "REDIS": 10, "JANUS": 25}


with gr.Blocks() as demo:
    gr.Markdown("## ExplainFuzz")

    with gr.Row():
        domain = gr.Radio(
            ["SQL", "B", "REDIS", "JANUS"], label="Choose Domain", value="SQL"
        )

        gr.Markdown("")

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
            max_length = max_length_mapping.get(domain, 10) - 2
            return (
                gr.update(visible=(count >= 1), interactive=(count >= 1)),
                gr.update(visible=(count >= 2), interactive=(count >= 2)),
                gr.update(visible=(count >= 3), interactive=(count >= 3)),
                gr.update(visible=has_pos, interactive=has_pos, maximum=max_length),
            )

        question.change(
            fn=update_literal_dropdowns,
            inputs=[question, domain],
            outputs=[literal1, literal2, literal3, position],
        )

        prob_button = gr.Button("Get Probability")
        prob_output = gr.Label()

        def update_token_dropdowns(domain):
            tokens = get_tokens(domain)
            return (
                gr.update(choices=tokens, value=None, interactive=True),
                gr.update(choices=tokens, value=None, interactive=True),
                gr.update(choices=tokens, value=None, interactive=True),
                tokens,
            )

        domain.change(
            fn=update_token_dropdowns,
            inputs=domain,
            outputs=[literal1, literal2, literal3, token_list],
        )

        prob_button.click(
            fn=dispatch_probability_function,
            inputs=[domain, question, literal1, literal2, literal3, position, mode],
            outputs=prob_output,
        )

    with gr.Tab("🧬 Input Generator"):
        sql_conn = gr.Textbox(
            label="PostgreSQL Connection String",
            placeholder="dbname=? user=? password=? host=? port=?",
        )
        num_inputs = gr.Slider(10, 1000, value=500, step=10, label="Number of Inputs")
        generate_btn = gr.Button("Generate")
        output_file = gr.File()
        generation_status = gr.Label()

        def toggle_input_fields(domain):
            return gr.update(visible=(domain == "SQL"))

        domain.change(fn=toggle_input_fields, inputs=domain, outputs=sql_conn)

        def run_generation(domain, mode, sql_conn, num_inputs):
            generation_status = f"Generating {num_inputs} inputs for {domain}..."
            zip_file = generate_inputs(domain, mode, int(num_inputs), sql_conn)
            return zip_file, f"Done! Download the generated inputs."

        generate_btn.click(
            fn=run_generation,
            inputs=[domain, mode, sql_conn, num_inputs],
            outputs=[output_file, generation_status],
        )
if __name__ == "__main__":
    demo.launch()
