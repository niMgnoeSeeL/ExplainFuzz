import gradio as gr
import zipfile
import os

""""This is a dummy FE for now"""

# Dummy token lists for each domain
def get_tokens(domain):
    return {
        "SQL": ["SELECT", "FROM", "WHERE", "JOIN", "GROUP_BY", "ORDER_BY", "INSERT", "UPDATE"],
        "MLIR": ["func", "module", "return", "memref", "call", "affine.for"],
        "CloudFormation": ["Resources", "Type", "Properties", "Outputs", "Conditions", "Parameters"]
    }.get(domain, [])

def get_query(query_type):
    return {
    "Marginal": ["MCQ 1", "MCQ 2", "MCQ 3"],
    "Conditional": ["Code 1", "Code 2"],
    "Evi": ["Written 1", "Written 2", "Written 3"],
    "Mmap": ["MMAR A", "MMAR B"]}.get(query_type, [])

def compute_probability(domain, after_token, current_token):
    # Dummy logic for probability
    return f"Probability of seeing '{current_token}' after '{after_token}' in {domain}: 42%"

def generate_inputs(domain, sql_conn, num_inputs):
    # Simulate input generation
    output_folder = f"generated_{domain.lower()}_inputs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(num_inputs):
        with open(os.path.join(output_folder, f"input_{i}.txt"), "w") as f:
            f.write(f"Generated input {i+1} for {domain}\n")

    zip_filename = f"{output_folder}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(output_folder):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)

    return zip_filename

with gr.Blocks() as demo:
    gr.Markdown("## 🔄 Explainable Fuzzer")

    domain = gr.Radio(["SQL", "MLIR", "CloudFormation"], label="Choose Domain", value="SQL")

    # Token list state to manage current token suggestions
    token_list = gr.State(get_tokens("SQL"))

    with gr.Tab("🔢 Probability Query"):
        with gr.Row():
            radio = gr.Radio(
                choices=["Marginal", "Conditional", "Evi", "Mmap"],
                label="Query Type",
                value="Marginal",
                interactive=True
            )
            dropdown = gr.Dropdown(
                label="Query Options",
                choices=get_query("Marginal"),
                value=None,
                interactive=True
            )

        def update_dropdown(selected_type):
            return gr.update(choices=get_query(selected_type), value=None)

        radio.change(fn=update_dropdown, inputs=radio, outputs=dropdown)

        with gr.Row():
            after_token = gr.Dropdown(choices=get_tokens("SQL"), label="Previous Token")
            current_token = gr.Dropdown(choices=get_tokens("SQL"), label="Current Token")

        prob_button = gr.Button("Get Probability")
        prob_output = gr.Label()

        def update_token_dropdowns(domain):
            tokens = get_tokens(domain)
            return gr.update(choices=tokens, value=None), gr.update(choices=tokens, value=None), tokens

        domain.change(fn=update_token_dropdowns, inputs=domain, outputs=[after_token, current_token, token_list])

        prob_button.click(
            fn=compute_probability,
            inputs=[domain, after_token, current_token],
            outputs=prob_output
        )

    with gr.Tab("🧬 Input Generator"):
        sql_conn = gr.Textbox(label="PostgreSQL Connection String", placeholder="dbname=? user=? password=? host=? port=?")
        num_inputs = gr.Slider(10, 10000, value=1000, step=10, label="Number of Inputs")
        generate_btn = gr.Button("Generate")
        output_file = gr.File()
        generation_status = gr.Label()

        def toggle_input_fields(domain):
            return gr.update(visible=(domain == "SQL"))

        domain.change(fn=toggle_input_fields, inputs=domain, outputs=sql_conn)

        def run_generation(domain, sql_conn, num_inputs):
            generation_status = f"Generating {num_inputs} inputs for {domain}..."
            zip_file = generate_inputs(domain, sql_conn, int(num_inputs))
            return zip_file, f"Done! Download the generated inputs."

        generate_btn.click(
            fn=run_generation,
            inputs=[domain, sql_conn, num_inputs],
            outputs=[output_file, generation_status]
        )
if __name__=="__main__":
    demo.launch()
