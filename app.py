from pathlib import Path
import gradio as gr
import zipfile
import os

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
    model, lit_map, lit_size, max_length = load_model_and_info(
        domain, mode
    )
    return ask_query(model, lit_map, lit_size, max_length, query_type, inputs)


def dispatch_probability_function(domain, question, lit1, lit2, mode):
    fn = question_to_function[question]
    if not fn:
        return "Unsupported question selected."

    count = literal_count_by_question[question]
    try:
        if count == 1:
            return fn(domain, lit1, mode)
        elif count == 2:
            return fn(domain, lit1, lit2, mode)
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

def prob_MAR2(domain, lit1, lit2, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token1 = literal_to_tokens[lit1]
    token2 = literal_to_tokens[lit2]
    inputs = [token1, token2]
    query_type = "MAR2"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit})={prob:.4f}"

def prob_COND1(domain, lit1, lit2, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token1 = literal_to_tokens[lit1]
    token2 = literal_to_tokens[lit2]
    inputs = [token1, token2]
    query_type = "COND1"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit1, lit2})={prob:.4f}"

def prob_COND2(domain, lit1, lit2, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token1 = literal_to_tokens[lit1]
    token2 = literal_to_tokens[lit2]
    inputs = [token1, token2]
    query_type = "COND2"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit})={prob:.4f}"

def prob_MMAP1(domain, lit, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    inputs = [token]
    query_type = "MMAP1"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit})={prob:.4f}"

def prob_MMAP2(domain, lit, mode):
    literal_to_tokens = get_literal_token_mapping(domain)
    token = literal_to_tokens[lit]
    inputs = [token]
    query_type = "MMAP2"
    prob = compute_probability(domain, query_type, inputs, mode)
    return f"P({lit})={prob:.4f}"
   


def generate_inputs(domain, mode, num_inputs, sql_conn=None):
    filename = main_generate_inputs(
        domain, mode, nb_concrete_inputs=num_inputs, conninfo=sql_conn
    )
    return filename

questions_by_type = {
    "Marginal": ["Marginal_1", "Marginal_2"],
    "Conditional": ["Conditional_1", "Conditional_2"],
    "Marginal Map": ["MarginalMap_1"],
    "Direct Evidence": ["DirectEvidence_1"]
}

question_description = {
    "Marginal_1": "P(Literal 1)",
    "Marginal_2": "P(Literal 1, Literal 2)",
    "Conditional_1": "P(Literal 1 | Literal 2), where Literal 2 appears anywhere after Literal 1",
    "Conditional_2": "P(Literal 1 | Literal 2), where Literal 2 appears immediately after Literal 1",
    "MarginalMap_1": "What is the most likely next literal after Literal 1?",
    "DirectEvidence_1": "....",

}

literal_count_by_question = {
    "Marginal_1": 1,
    "Marginal_2": 2,
    "Conditional_1": 2,
    "Conditional_2": 2,
    "MarginalMap_1": 1,
    "DirectEvidence_1": 1,
}

question_to_function = {
    "Marginal_1": prob_MAR1,
    "Marginal_2": prob_MAR2,
    "Conditional_1": prob_COND1,
    "Conditional_2": prob_COND2,
    "MarginalMap_1": prob_MMAP1,
    "DirectEvidence_1": prob_MMAP2,
}


with gr.Blocks() as demo:
    gr.Markdown("## 🔄 Explainable Fuzzer")
    
    with gr.Row():
        domain = gr.Radio(
            ["SQL", "B", "REDIS", "JANUS"], label="Choose Domain", value="SQL"
        )

        gr.Markdown("")
        
        mode = gr.Radio(["generate", "no-generate"], value="no-generate", label="Mode:", interactive=True)


    # Token list state to manage current token suggestions
    token_list = gr.State(get_tokens("SQL"))

    

    with gr.Tab("🔢 Probability Query"):
        with gr.Row():
            query_type = gr.Radio(
                choices=list(questions_by_type.keys()),
                label="Query Type",
                value="Marginal"
            )
            question = gr.Dropdown(
                choices=[(question_description[q], q) for q in questions_by_type["Marginal"]],
                label="Question"
            )

        with gr.Row():
            literal1 = gr.Dropdown(choices=get_tokens("SQL"), label="Literal 1", visible=True)
            literal2 = gr.Dropdown(choices=get_tokens("SQL"), label="Literal 2", visible=False)

        # Update function
        def update_question_choices(qtype):
            return gr.update(choices=[(question_description[q], q) for q in questions_by_type[qtype]], value=None)

        query_type.change(
            fn=update_question_choices,
            inputs=query_type,
            outputs=question
        )

        # When question changes, update literals
        def update_literal_dropdowns(q):
            count = literal_count_by_question.get(q, 1)
            return (
                gr.update(visible=True, interactive=(count == 2)),
                gr.update(visible=(count == 2), interactive=(count == 2)),
            )

        question.change(
            fn=update_literal_dropdowns,
            inputs=question,
            outputs=[literal1, literal2]
        )

        prob_button = gr.Button("Get Probability")
        prob_output = gr.Label()

        def update_token_dropdowns(domain):
            tokens = get_tokens(domain)
            return (
                gr.update(choices=tokens, value=None, interactive=True),
                gr.update(choices=tokens, value=None, interactive=True),
                tokens,
            )

        domain.change(
            fn=update_token_dropdowns,
            inputs=domain,
            outputs=[literal1, literal2, token_list],
        )

        prob_button.click(
            fn=dispatch_probability_function,
            inputs=[domain, question, literal1, literal2, mode],
            outputs=prob_output,
        )

    with gr.Tab("🧬 Input Generator"):
        sql_conn = gr.Textbox(
            label="PostgreSQL Connection String",
            placeholder="dbname=? user=? password=? host=? port=?",
        )
        num_inputs = gr.Slider(10, 10000, value=1000, step=10, label="Number of Inputs")
        generate_btn = gr.Button("Generate")
        output_file = gr.File()
        generation_status = gr.Label()

        def toggle_input_fields(domain):
            return gr.update(visible=(domain == "SQL"))

        domain.change(fn=toggle_input_fields, inputs=domain, outputs=sql_conn)

        def run_generation(domain, sql_conn, num_inputs):
            mode = "no-generate"
            generation_status = f"Generating {num_inputs} inputs for {domain}..."
            zip_file = generate_inputs(domain, mode, int(num_inputs), sql_conn)
            return zip_file, f"Done! Download the generated inputs."

        generate_btn.click(
            fn=run_generation,
            inputs=[domain, sql_conn, num_inputs],
            outputs=[output_file, generation_status],
        )
if __name__ == "__main__":
    demo.launch()
