from grammarinator_fuzzing.filter_inputs import read_queries_from_file, test_inputs_SUT_from_folder, test_inputs_on_SUT
from main import main_generate_inputs
import json
import matplotlib.pyplot as plt
import os
import numpy as np
from collections import defaultdict


def eval_bug_rate_Grammarinator(required_tokens,sensitive_fields):
    print("On the train dataset")
    nb_train_inputs = 8995
    folder_path = "data/intermediate/dataset/SQL/no-generate/train/"
    failing_rate_train, executable_rate_train = test_inputs_SUT_from_folder(folder_path,required_tokens,sensitive_fields)

    print("On the test dataset")
    nb_test_inputs = 999
    folder_path = "data/intermediate/dataset/SQL/no-generate/test/"
    failing_rate_test, executable_rate_test = test_inputs_SUT_from_folder(folder_path,required_tokens,sensitive_fields)

    failing_rate_global = round((failing_rate_train*nb_train_inputs + failing_rate_test*nb_test_inputs)/(nb_train_inputs+nb_test_inputs),2)
    executable_rate_global = round((executable_rate_test*nb_test_inputs + executable_rate_train*nb_train_inputs)/(nb_train_inputs+nb_test_inputs),2)
    print(f"Global failing rate for Grammarinator is {failing_rate_global}% and the executable rate is {executable_rate_global}% for a total of {nb_train_inputs+nb_test_inputs} tests")
    return {"train": {"failing_rate":failing_rate_train, "executable_rate" :executable_rate_train}, "test": {"failing_rate":failing_rate_test, "executable_rate" :executable_rate_test}, "global": {"failing_rate":failing_rate_global, "executable_rate" :executable_rate_global}}

def eval_bug_rate_ExplainFuzz(required_tokens,sensitive_fields,token_condition=None):
    # Check the bug rate of generated inputs by ExplainFuzz + custom generator on the SUT
    
    # 2) Test them on the SUT
    print("On the generated dataset by ExplainFuzz")
    file_path = "data/output/inputs/SQL/inputs_no_generate.txt"
    queries = read_queries_from_file(file_path)
    failing_rate,executable_rate = test_inputs_on_SUT(queries,required_tokens,sensitive_fields)
    print(f"Global failing rate for the ExplainFuzz {'with conditon' + token_condition if token_condition else ''} is {failing_rate}% and the executable rate is {executable_rate}%")
    return {"global":{"failing_rate":failing_rate, "executable_rate" :executable_rate}}

def eval_bug_rate_seeds(required_tokens,sensitive_fields):
    folder_path = "data/input/seeds/SQL/"
    failing_rate, executable_rate = test_inputs_SUT_from_folder(folder_path,required_tokens,sensitive_fields)
    print(f"Global failing rate for the seeds is {failing_rate}% and the executable rate is {executable_rate}%")
    return {"global": {"failing_rate":failing_rate, "executable_rate" :executable_rate}}




def run_eval(file_path="evaluation_bug_rate_results.json",domain="SQL",mode="no-generate",num_inputs=10000):
    # tokens_to_tests = [None,"ORDER","JOIN","GROUP","HAVING","WHERE","USING","SELECT"]
    # sensitive_fields_to_tests = [None,"ssn_number","email","salary"]
    tokens_to_tests = ["ORDER","JOIN","WHERE","OR"]
    sensitive_fields_to_tests = [None,"ssn_number","email","salary"]
   

    mapping_key_words_to_token = {
        None: None,
        "ORDER": "ORDER",
        "JOIN": "JOIN",
        "GROUP": "GROUP_P",
        "HAVING": "HAVING",
        "WHERE": "WHERE",
        "USING": "USING",
        "SELECT": "SELECT",
        "OR": "OR",
        "UNION": "UNION"
    }

    # Load existing results if file already exists
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                res_list = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Warning: JSON file was corrupt or empty, starting fresh.")
            res_list = []
    else:
        res_list = []

    # Keep track of combinations already done
    completed = {(r["token"], r["sensitive"],r["with_condition"]) for r in res_list}

    for tok in tokens_to_tests:
        token_condition = mapping_key_words_to_token[tok]
        main_generate_inputs(domain, mode, num_inputs,token_condition)
        for sensitive in sensitive_fields_to_tests:
            if (tok, sensitive) in completed:
                print(f"⏩ Skipping already completed: token={tok}, sensitive={sensitive}")
                continue
            

            print(f"########## Testing for token {tok} and sensitive field {sensitive}")

            required_tokens = [tok] if tok is not None else None
            sensitive_fields = [sensitive] if sensitive is not None else None

            

            res_grammarinator = eval_bug_rate_Grammarinator(required_tokens, sensitive_fields)
            res_seeds = eval_bug_rate_seeds(required_tokens, sensitive_fields)

            
            res_explainfuzz_with_condition = eval_bug_rate_ExplainFuzz(required_tokens, sensitive_fields)
            

            result_entry = {
                "token": tok,
                "sensitive": sensitive,
                "with_condition":True,
                "Grammarinator": res_grammarinator,
                "ExplainFuzz + conditioning": res_explainfuzz_with_condition,
                "seeds": res_seeds
            }

            # Append to list in memory
            res_list.append(result_entry)

    with_condition = False
    main_generate_inputs(domain, mode, num_inputs,None)
    for tok in tokens_to_tests:
        for sensitive in sensitive_fields_to_tests:
            if (tok, sensitive,with_condition) in completed:
                print(f"⏩ Skipping already completed: token={tok}, sensitive={sensitive}")
                continue
            

            print(f"########## Testing for token {tok} and sensitive field {sensitive}")

            required_tokens = [tok] if tok is not None else None
            sensitive_fields = [sensitive] if sensitive is not None else None
            
            res_explainfuzz_no_condition = eval_bug_rate_ExplainFuzz(required_tokens, sensitive_fields)
            
            for res in res_list:
                if res["token"]==tok and res["sensitive"]==sensitive:
                    res["ExplainFuzz"]=res_explainfuzz_no_condition

            # Save incrementally
            with open(file_path, "w") as f:
                json.dump(res_list, f, indent=4, default=str)

            print(f"✅ Saved result for token={tok}, sensitive={sensitive}\n")

    print(f"🎉 Evaluation complete. Results saved to {file_path}")
    return res_list
    

def visualize_bug_eval_results_with_error(file_path="evaluation_bug_rate_results.json"):
    # === Load results ===
    with open(file_path, "r") as f:
        results = json.load(f)

    # === Group results by (token, sensitive) ===
    grouped = defaultdict(lambda: {
        "grammarinator_exec": [],
        "grammarinator_fail": [],
        "explainfuzz_exec": [],
        "explainfuzz_fail": [],
        "explainfuzz_cond_exec": [],
        "explainfuzz_cond_fail": [],
        "seeds_exec": [],
        "seeds_fail": []
    })

    for entry in results:
        token = entry["token"] or "None"
        sensitive = entry["sensitive"] or "None"
        key = (token, sensitive)

        g = entry["Grammarinator"]["global"]
        e = entry["ExplainFuzz"]["global"]
        ec = entry["ExplainFuzz + conditioning"]["global"]
        s = entry["seeds"]["global"]

        grouped[key]["grammarinator_exec"].append(g["executable_rate"])
        grouped[key]["grammarinator_fail"].append(g["failing_rate"])
        grouped[key]["explainfuzz_exec"].append(e["executable_rate"])
        grouped[key]["explainfuzz_fail"].append(e["failing_rate"])
        grouped[key]["seeds_exec"].append(s["executable_rate"])
        grouped[key]["seeds_fail"].append(s["failing_rate"])
        grouped[key]["explainfuzz_cond_exec"].append(ec["executable_rate"])
        grouped[key]["explainfuzz_cond_fail"].append(ec["failing_rate"])

    # === Aggregate ===
    labels = []
    g_exec_means, g_exec_stds = [], []
    g_fail_means, g_fail_stds = [], []
    e_exec_means, e_exec_stds = [], []
    e_fail_means, e_fail_stds = [], []
    ec_exec_means, ec_exec_stds = [], []
    ec_fail_means, ec_fail_stds = [], []
    s_exec_means, s_exec_stds = [], []
    s_fail_means, s_fail_stds = [], []

    for (token, sensitive), vals in grouped.items():
        label = f"{token}\n({sensitive})"
        labels.append(label)

        g_exec = np.array(vals["grammarinator_exec"])
        g_fail = np.array(vals["grammarinator_fail"])
        e_exec = np.array(vals["explainfuzz_exec"])
        e_fail = np.array(vals["explainfuzz_fail"])
        ec_exec = np.array(vals["explainfuzz_cond_exec"])
        ec_fail = np.array(vals["explainfuzz_cond_fail"])
        s_exec = np.array(vals["seeds_exec"])
        s_fail = np.array(vals["seeds_fail"])

        g_exec_means.append(g_exec.mean())
        g_exec_stds.append(g_exec.std())
        g_fail_means.append(g_fail.mean())
        g_fail_stds.append(g_fail.std())
        e_exec_means.append(e_exec.mean())
        e_exec_stds.append(e_exec.std())
        e_fail_means.append(e_fail.mean())
        e_fail_stds.append(e_fail.std())
        ec_exec_means.append(ec_exec.mean())
        ec_exec_stds.append(ec_exec.std())
        ec_fail_means.append(ec_fail.mean())
        ec_fail_stds.append(ec_fail.std())
        s_exec_means.append(s_exec.mean())
        s_exec_stds.append(s_exec.std())
        s_fail_means.append(s_fail.mean())
        s_fail_stds.append(s_fail.std())

    x = np.arange(len(labels))
    width = 0.10  # Smaller width for 3 bars side-by-side

    colors = {
        "Grammarinator": "#1f77b4",  # blue
        "ExplainFuzz": "#ff7f0e",    # orange
        "Seeds": "#2ca02c",
                   "ExplainFuzz + conditioning": "#ff160e",    # orange           # green
    }

    # === Executable rate plot ===
    plt.figure(figsize=(11, 5))
    plt.bar(x - 2*width, g_exec_means, width, yerr=g_exec_stds, 
            label='Grammarinator', capsize=5, alpha=0.85, color=colors["Grammarinator"])
    plt.bar(x - width, e_exec_means, width, yerr=e_exec_stds, 
            label='ExplainFuzz', capsize=5, alpha=0.85, color=colors["ExplainFuzz"])
    plt.bar(x + width, ec_exec_means, width, yerr=ec_exec_stds, 
            label='ExplainFuzz + conditioning', capsize=5, alpha=0.85, color=colors["ExplainFuzz + conditioning"])
    # plt.bar(x + 2*width, s_exec_means, width, yerr=s_exec_stds, 
    #         label='Seeds', capsize=5, alpha=0.85, color=colors["Seeds"])

    plt.ylabel('Executable rate (%)', fontsize=12)
    plt.title('Executable Rate Comparison (mean ± std)', fontsize=14, fontweight='bold')
    plt.xticks(x, labels, rotation=25, ha="right")
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.show()

    # === Failing rate plot ===
    plt.figure(figsize=(11, 5))
    plt.bar(x - 2*width, g_fail_means, width, yerr=g_fail_stds, 
            label='Grammarinator', capsize=5, alpha=0.85, color=colors["Grammarinator"])
    plt.bar(x - width, e_fail_means, width, yerr=e_fail_stds, 
            label='ExplainFuzz', capsize=5, alpha=0.85, color=colors["ExplainFuzz"])
    plt.bar(x + width, ec_fail_means, width, yerr=ec_fail_stds, 
            label='ExplainFuzz + conditioning', capsize=5, alpha=0.85, color=colors["ExplainFuzz + conditioning"])
    plt.bar(x + 2*width, s_fail_means, width, yerr=s_fail_stds, 
            label='Seeds', capsize=5, alpha=0.85, color=colors["Seeds"])

    plt.ylabel('Failing (bug) rate (%)', fontsize=12)
    plt.title('Failing Rate Comparison (mean ± std)', fontsize=14, fontweight='bold')
    plt.xticks(x, labels, rotation=25, ha="right")
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    # res_list = run_eval("data/new_results/bug_rate/eval_after_gen_improved.json")
    visualize_bug_eval_results_with_error("data/new_results/bug_rate/eval_after_gen_improved.json")
    #visualize_bug_eval_results_with_error("data/new_results/bug_rate/eval_bug_rate_with_seeds.json")
    # eval_bug_rate_seeds(["ORDER"],None)
    