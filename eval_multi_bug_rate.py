from grammarinator_fuzzing.SUT import check_multi_bug
from grammarinator_fuzzing.filter_inputs import measure_multi_bug_rate, measure_multi_bug_rate_from_folder, read_queries_from_file, test_inputs_SUT_from_folder, test_inputs_on_SUT
from main import main_generate_inputs
import json
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

def eval_multi_bug_rate(source: str, path: str, from_file: bool = False):
    """
    Evaluate multi-bug rate for a given data source.

    Args:
        source (str): Name of the source (e.g., 'Grammarinator', 'ExplainFuzz', 'Seeds')
        path (str): Path to folder or file
        from_file (bool): Whether to read from a single file or from a folder
    """
    print(f"Evaluating {source}...")

    if from_file:
        queries = read_queries_from_file(path)
        res = measure_multi_bug_rate(queries)
    else:
        res = measure_multi_bug_rate_from_folder(path)

    return res


# Convenience wrappers for readability
def eval_multi_bug_rate_Grammarinator():
    return eval_multi_bug_rate(
        source="Grammarinator",
        path="data/intermediate/dataset/SQL/no-generate/train/",
        from_file=False
    )

def eval_multi_bug_rate_ExplainFuzz():
    return eval_multi_bug_rate(
        source="ExplainFuzz",
        path="data/output/inputs/SQL/inputs_no_generate.txt",
        from_file=True
    )

def eval_multi_bug_rate_seeds():
    return eval_multi_bug_rate(
        source="Seeds",
        path="data/input/seeds/SQL/",
        from_file=False
    )


def run_eval_multi_bug(file_path,domain="SQL",mode="no-generate",num_inputs=10000):
    results = {}
    res_Seeds = eval_multi_bug_rate_seeds()
    res_grammarinator = eval_multi_bug_rate_Grammarinator()
    main_generate_inputs(domain, mode, num_inputs,None)
    res_ExplainFuzz = eval_multi_bug_rate_ExplainFuzz()

    results["Grammarinator"]=res_grammarinator
    results["ExplainFuzz"]=res_ExplainFuzz
    results["Seeds"] = res_Seeds

    with open(file_path, "w") as f:
        json.dump(results, f, indent=4, default=str)
    
    print(f"🎉 Evaluation complete. Results saved to {file_path}")

    return results

def visualize_multi_bug_results(file_path):
    """
    Visualize multi-bug evaluation results for different fuzzers.
    
    Args:
        results (dict): Dictionary of results like:
            {
                "Grammarinator": {...},
                "ExplainFuzz": {...},
                ...
            }
    """
    # ---- Summary Table ----

    with open(file_path, "r") as f:
        results = json.load(f)

    summary_data = []
    for fuzzer, data in results.items():
        summary_data.append({
            "Fuzzer": fuzzer,
            "Coverage (%)": data["coverage"],
            "Total Triggers": data["total_triggers"]
        })
    summary_df = pd.DataFrame(summary_data)

    print("=== Summary ===")
    print(summary_df.to_string(index=False))

    # ---- Per-Bug Counts ----
    # Flatten per-bug results
    bug_rows = []
    for fuzzer, data in results.items():
        for bug, count in data["per_bug_counts"].items():
            bug_rows.append({"Fuzzer": fuzzer, "Bug": bug, "Triggers": count})
    bug_df = pd.DataFrame(bug_rows)

    # Pivot for grouped bar chart
    pivot_df = bug_df.pivot(index="Bug", columns="Fuzzer", values="Triggers").fillna(0)

    # ---- Plot ----
    pivot_df.plot(kind="bar", figsize=(10, 6))
    plt.title("Bug Triggers per Fuzzer")
    plt.xlabel("Bug ID")
    plt.ylabel("Number of Triggers")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.legend(title="Fuzzer")
    plt.tight_layout()
    plt.show()

    # ---- Optional: Coverage bar ----
    plt.figure(figsize=(6, 4))
    plt.bar(summary_df["Fuzzer"], summary_df["Coverage (%)"])
    plt.title("Bug Coverage per Fuzzer")
    plt.ylabel("Coverage (%)")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    #results = run_eval_multi_bug("data/new_results/bug_rate/eval_multi_bug.json")
    visualize_multi_bug_results("data/new_results/bug_rate/eval_multi_bug.json")
    