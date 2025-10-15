from grammarinator_fuzzing.filter_inputs import measure_multi_bug_rate, measure_multi_bug_rate_from_folder, read_queries_from_file
from main import RESULTS_DIR, main_generate_inputs
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def eval_multi_bug_rate(source: str, path: str, from_file: bool = False,bug_specs={}):
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
        res = measure_multi_bug_rate(queries,bug_specs)
    else:
        res = measure_multi_bug_rate_from_folder(path,bug_specs)

    return res


# Convenience wrappers for readability
def eval_multi_bug_rate_Grammarinator(bug_specs):
    return eval_multi_bug_rate(
        source="Grammarinator",
        path="data/intermediate/dataset/SQL/no-generate/train/",
        from_file=False,
        bug_specs=bug_specs
    )

def eval_multi_bug_rate_ExplainFuzz(bug_specs):
    return eval_multi_bug_rate(
        source="ExplainFuzz",
        path="data/output/inputs/SQL/inputs_no_generate.txt",
        from_file=True,
        bug_specs=bug_specs
    )

def eval_multi_bug_rate_seeds(bug_specs):
    return eval_multi_bug_rate(
        source="Seeds",
        path="data/input/seeds/SQL/",
        from_file=False,
        bug_specs =bug_specs
    )


def run_eval_multi_bug(file_path=None,domain="SQL",mode="no-generate",num_inputs=10000,R=5):
    bug_specs = {
    "BUG1_select_email": {
        "required": ["SELECT"],
        "sensitive": ["email"]
    },
    "BUG2_salary_update": {
        "required": ["UPDATE"],
        "sensitive": ["salary"]
    },
    "BUG3_join_ssn": {
        "required": ["JOIN"],
        "sensitive": ["ssn_number"]
    },
    "BUG4_select_budget": {
        "required": ["SELECT"],
        "sensitive": ["budget"]
    },
    "BUG5_join_ssn_email": {
        "required": ["JOIN"],
        "sensitive": ["ssn_number", "email"]
    },
    "BUG6_join_sensitive_data": {
        "required": ["JOIN"],
        "sensitive": ["email", "ssn_number", "salary"]
    },
    "BUG7_where_name_email": {
        "required": ["WHERE"],
        "sensitive": ["employee_name", "email"]
    },
    "BUG8_where_name_ssn": {
        "required": ["WHERE"],
        "sensitive": ["employee_name", "ssn_number"]
    },
    "BUG9_nested_select_ssn": {
        "required": ["SELECT", "FROM", "SELECT"],
        "sensitive": ["ssn_number"]
    },
    "BUG10_where_or_salary": {
        "required": ["WHERE", "OR"],
        "sensitive": ["salary"]
    },"BUG11_union": {
        "required": ["UNION"],
        "sensitive": ["salary"]
    }
}
    
    results = {}
    res_Seeds = eval_multi_bug_rate_seeds(bug_specs)
    res_grammarinator = eval_multi_bug_rate_Grammarinator(bug_specs)
    res_ExplainFuzz = []
    for _ in range(R):
        main_generate_inputs(domain, mode, num_inputs,None)
        res_ExplainFuzz_k = eval_multi_bug_rate_ExplainFuzz(bug_specs)
        res_ExplainFuzz.append(res_ExplainFuzz_k)

    results["Seeds"] = res_Seeds
    results["Grammarinator"]=res_grammarinator
    results["ExplainFuzz"]=res_ExplainFuzz
    
    if not file_path:
        file_name = f"results_multi_bug_{domain}.json"
        folder_path = RESULTS_DIR / "bug_rate"
        file_path =  folder_path / file_name

    with open(file_path, "w") as f:
        json.dump(results, f, indent=4, default=str)
    
    print(f"🎉 Evaluation complete. Results saved to {file_path}")
    visualize_multi_bug_results(file_path)
    return results

def visualize_multi_bug_results(file_path):
    """
    Visualize multi-bug evaluation results for different fuzzers.
    
    Supports multiple runs for ExplainFuzz (list of dicts).

    Args:
        file_path (str): Path to JSON file containing results.
    """
    with open(file_path, "r") as f:
        results = json.load(f)

    summary_data = []
    bug_rows = []

    for fuzzer, data in results.items():
        # Handle ExplainFuzz: list of runs
        if isinstance(data, list):
            coverages = [run["coverage"] for run in data]
            total_triggers = [run["total_triggers"] for run in data]

            mean_cov = np.mean(coverages)
            std_cov = np.std(coverages)
            mean_trig = np.mean(total_triggers)
            std_trig = np.std(total_triggers)

            summary_data.append({
                "Fuzzer": fuzzer,
                "Coverage (%)": f"{mean_cov:.1f} ± {std_cov:.1f}",
                "Total Triggers": f"{mean_trig:.1f} ± {std_trig:.1f}"
            })

            # Aggregate per-bug stats across runs
            all_bug_counts = {}
            for run in data:
                for bug, count in run["per_bug_counts"].items():
                    all_bug_counts.setdefault(bug, []).append(count)

            for bug, counts in all_bug_counts.items():
                bug_rows.append({
                    "Fuzzer": fuzzer,
                    "Bug": bug,
                    "Mean Triggers": np.mean(counts),
                    "Std Triggers": np.std(counts)
                })
        else:
            # Single result (Grammarinator, Seeds, etc.)
            summary_data.append({
                "Fuzzer": fuzzer,
                "Coverage (%)": data["coverage"],
                "Total Triggers": data["total_triggers"]
            })

            for bug, count in data["per_bug_counts"].items():
                bug_rows.append({
                    "Fuzzer": fuzzer,
                    "Bug": bug,
                    "Mean Triggers": count,
                    "Std Triggers": 0
                })

    # ---- Print summary ----
    summary_df = pd.DataFrame(summary_data)
    print("=== Summary ===")
    print(summary_df.to_string(index=False))

    # ---- Per-bug plot ----
    bug_df = pd.DataFrame(bug_rows)
    pivot_mean = bug_df.pivot(index="Bug", columns="Fuzzer", values="Mean Triggers").fillna(0)
    pivot_std = bug_df.pivot(index="Bug", columns="Fuzzer", values="Std Triggers").fillna(0)

    # Plot with error bars
    ax = pivot_mean.plot(kind="bar", yerr=pivot_std, figsize=(10, 6), capsize=4)
    plt.title("Bug Triggers per Fuzzer (mean ± std)")
    plt.xlabel("Bug ID")
    plt.ylabel("Number of Triggers")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.legend(title="Fuzzer")
    plt.tight_layout()
    plt.show()

    # ---- Coverage plot ----
    plt.figure(figsize=(6, 4))
    bars = []
    labels = []
    for fuzzer, data in results.items():
        if isinstance(data, list):
            coverages = [run["coverage"] for run in data]
            plt.bar(fuzzer, np.mean(coverages), yerr=np.std(coverages), capsize=5)
        else:
            plt.bar(fuzzer, data["coverage"])
    plt.title("Bug Coverage per Fuzzer (mean ± std)")
    plt.ylabel("Coverage (%)")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    results= run_eval_multi_bug(R=1)
    # visualize_multi_bug_results("data/results/bug_rate/results_multi_bug_SQL.json")
    