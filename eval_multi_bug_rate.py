from bug_specs import BUG_SPECS
from grammarinator_fuzzing.filter_inputs import measure_multi_bug_rate, measure_multi_bug_rate_from_folder, read_queries_from_file
from main import RESULTS_DIR, main_generate_inputs
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def eval_multi_bug_rate(source: str, path: str, from_file: bool = False,bug_specs={}, scenario=1):
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
        res = measure_multi_bug_rate(queries,bug_specs,scenario)
    else:
        res = measure_multi_bug_rate_from_folder(path,bug_specs,scenario)

    return res


# Convenience wrappers for readability
def eval_multi_bug_rate_Grammarinator(domain,scenario):
    return eval_multi_bug_rate(
        source="Grammarinator",
        path=f"data/intermediate/dataset/{domain}/no-generate/train/",
        from_file=False,
        bug_specs=BUG_SPECS,
         scenario=scenario
    )

def eval_multi_bug_rate_ExplainFuzz(domain,scenario):
    return eval_multi_bug_rate(
        source="ExplainFuzz",
        path=f"data/output/inputs/{domain}/inputs_no_generate.txt",
        from_file=True,
        bug_specs=BUG_SPECS,
         scenario=scenario
    )

def eval_multi_bug_rate_seeds(domain,scenario):
    domain_seeds = domain[:-1] if domain[-1]=="A" or domain[-1]=="B" else domain
    return eval_multi_bug_rate(
        source="Seeds",
        path=f"data/input/seeds/{domain_seeds}/",
        from_file=False,
        bug_specs =BUG_SPECS,
        scenario=scenario
    )


def run_eval_multi_bug(domain="SQL",mode="no-generate",num_inputs=10000,R=5,file_path=None,scenario=1):
    results = {}
    res_Seeds = eval_multi_bug_rate_seeds(domain,scenario)
    res_grammarinator = eval_multi_bug_rate_Grammarinator(domain,scenario)
    res_ExplainFuzz = []
    for _ in range(R):
        main_generate_inputs(domain, mode, num_inputs,None)
        res_ExplainFuzz_k = eval_multi_bug_rate_ExplainFuzz(domain,scenario)
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

    return results

def visualize_multi_bug_results(file_path=None,results=None):
    """
    Visualize multi-bug evaluation results for different fuzzers.
    
    Supports multiple runs for ExplainFuzz (list of dicts).

    Args:
        file_path (str): Path to JSON file containing results.
    """
    if not file_path and not results:
        raise Exception("Need to provide at least a file_path or some results")
    
    if file_path:
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
                if fuzzer == "Seeds":
                    bug_rows.append({
                        "Fuzzer": fuzzer,
                        "Bug": bug,
                        "Mean Triggers": count*100,
                        "Std Triggers": 0
                    })
                else:
                    bug_rows.append({
                        "Fuzzer": fuzzer,
                        "Bug": bug,
                        "Mean Triggers": count,
                        "Std Triggers": 0
                    })


    colors = {
        "Grammarinator": "#1f77b4",  # blue
        "ExplainFuzz": "#ff7f0e",    # orange
        "Seeds": "#2ca02c",
                   "ExplainFuzz + conditioning": "#ff160e",    # orange           # green
    }
    # ---- Print summary ----
    summary_df = pd.DataFrame(summary_data)
    print("=== Summary ===")
    print(summary_df.to_string(index=False))

    # ---- Per-bug plot ----
    bug_df = pd.DataFrame(bug_rows)
    pivot_mean = bug_df.pivot(index="Bug", columns="Fuzzer", values="Mean Triggers").fillna(0)
    pivot_std = bug_df.pivot(index="Bug", columns="Fuzzer", values="Std Triggers").fillna(0)

    color_list = [colors[f] for f in pivot_mean.columns]
    # Plot with error bars
    ax = pivot_mean.plot(kind="bar", yerr=pivot_std, figsize=(10, 6), capsize=4,color=color_list)
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
        c = colors.get(fuzzer, "#808080")
        if isinstance(data, list):
            coverages = [run["coverage"] for run in data]
            plt.bar(fuzzer, np.mean(coverages), yerr=np.std(coverages), capsize=5,color = c)
        else:
            plt.bar(fuzzer, data["coverage"],color=c)
    plt.title("Bug Coverage per Fuzzer (mean ± std)")
    plt.ylabel("Coverage (%)")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def aggregate_results_per_seed(seed_results, keys):
    """Aggregate ExplainFuzz runs for one seed set.
    
    Handles both scalar keys and per-bug dictionary keys.
    """
    agg = {}
    for key in keys:
        # Check if the first run[key] is a dict (per-bug metric)
        if isinstance(seed_results[0][key], dict):
            # Collect all bug IDs
            
            bug_ids = set()
            for seed_res in seed_results:
                for bug_trig in seed_res[key].keys():
                    bug_ids.add(bug_trig)
            print(bug_ids)
            agg[key] = {}
            for bug in bug_ids:
                vals = [run.get(key,{}).get(bug, 0) for run in seed_results]
                agg[key][bug] = {
                    "mean": np.mean(vals),
                    "std": np.std(vals)
                }
        else:
            # Scalar metric
            vals = [run[key] for run in seed_results]
            agg[key] = {
                "mean": np.mean(vals),
                "std": np.std(vals)
            }
    return agg
def filter_results_key(result, keys):
    """
    Return a new dictionary containing only the specified top-level keys from `result`.
    
    Args:
        result (dict): the full results dictionary
        keys (list of str): list of keys to keep
    
    Returns:
        dict: filtered dictionary
    """
    return {k: result[k] for k in keys if k in result}

def get_final_summary_multi_bug_evaluation(keys,file_path_summary):
    # keys = ["executable_rate", "nb_distinct_bugs_triggered", "coverage",
    #         "total_triggers", "total_distinct_queries", 
    #         "avg_inputs_per_bug", "avg_distinct_per_bug","explicit_sensitive"]
    
    final_summary={}
    for domain in ["SQL1A","SQL2A","SQL3A","SQL4A"]:
        file_path = f"data/results/multi_bug_rate/scenario_2_results_multi_bug_{domain}.json"
        with open(file_path, "r") as f:
            results = json.load(f)
        res_grammarinator = filter_results_key(results["Grammarinator"],keys)
        res_explainfuzz = aggregate_results_per_seed(results["ExplainFuzz"],keys)
        final_summary[domain]={"Grammarinator":res_grammarinator,"ExplainFuzz":res_explainfuzz}

    # file_path_summary = "data/results/multi_bug_rate/summary_results_multi_bug.json"
    with open(file_path_summary, "w") as f:
        json.dump(final_summary, f, indent=4, default=str)



def plot_per_bug_bar(gramm_data, ef_data, bug_specs, metric="per_bug_counts_distinct"):
    """
    Plot a bar chart comparing Grammarinator vs ExplainFuzz per bug.
    
    gramm_data: dict from Grammarinator (scalar or per-bug values)
    ef_data: dict from ExplainFuzz aggregated results (mean/std per bug)
    bug_specs: dict of all bugs to include (keys are bug IDs)
    metric: "per_bug_counts_distinct" or "per_bug_explicit_sensitive"
    """
    bug_ids = list(bug_specs.keys())
    n_bugs = len(bug_ids)
    
    gramm_vals = [gramm_data[metric].get(bug, 0) for bug in bug_ids]
    
    ef_means = [ef_data[metric].get(bug,{}).get("mean",0) for bug in bug_ids]
    ef_stds = [ef_data[metric].get(bug,{}).get("std",0) for bug in bug_ids]
    
    x = np.arange(n_bugs)
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(15,5))
    
    rects1 = ax.bar(x - width/2, gramm_vals, width, label="Grammarinator", color="#1f77b4")
    rects2 = ax.bar(x + width/2, ef_means, width, yerr=ef_stds, capsize=5,
                    label="ExplainFuzz", color="#ff7f0e")
    
    ax.set_xlabel("Bug ID")
    ax.set_ylabel(metric.replace("_"," ").title())
    ax.set_title(f"Comparison per Bug: {metric.replace('_',' ').title()}")
    ax.set_xticks(x)
    ax.set_xticklabels(bug_ids, rotation=45, ha="right")
    ax.legend()
    
    plt.tight_layout()
    plt.show()

def vizualize_res(file_path):
    with open(file_path, "r") as f:
        results = json.load(f)
    for domain in ["SQL1A","SQL2A","SQL3A","SQL4A"]:
        res_domain = results[domain]
        gramm_data = res_domain["Grammarinator"]
        ef_data = res_domain["ExplainFuzz"]
        plot_per_bug_bar(gramm_data, ef_data, bug_specs=BUG_SPECS, metric=f"per_bug_counts_distinct for the seed {domain[-1]}")

def generate_table_per_trigger(file_path):
    with open(file_path, "r") as f:
        summary = json.load(f)

    bugs = list(BUG_SPECS.keys())
    seeds = ["SQL1A", "SQL2A", "SQL3A", "SQL4A"]
    models = ["Grammarinator", "ExplainFuzz"]

    rows = []
    for bug in bugs:
        row = {"Bug ID": bug.replace('_','\_')}
        trigger_counts = {model: 0 for model in models}

        for seed in seeds:
            for model in models:
                counts = summary[seed][model].get("per_bug_counts_distinct", {})
                if model == "ExplainFuzz":
                    counts = {k: v["mean"] for k, v in counts.items()}  # take mean

                triggered = bug in counts and counts[bug] > 0
                row[f"{seed} {model}"] = "\\cmark" if triggered else "\\xmark"
                if triggered:
                    trigger_counts[model] += 1

        # Compute % triggered per model
        for model in models:
            percent = 100 * trigger_counts[model] / len(seeds)
            row[f"{model} %"] = f"{percent:.0f}\\%"

        rows.append(row)

    df = pd.DataFrame(rows)

    # Optional: reorder columns so that percentage columns appear at the end
    ordered_cols = (
        ["Bug ID"]
        + [f"{s} {m}" for s in seeds for m in models]
        + [f"{m} %" for m in models]
    )
    df = df[ordered_cols]

    print(df.to_latex(index=False, escape=False)) 


# def add_per_bug_explicit_sensitive_metric_safe(json_path):
#     """
#     Load a JSON results file (per seed), compute the overall 'explicit_sensitive'
#     metric as the mean over 'per_bug_explicit_sensitive', and save it back.
#     Handles empty dictionaries safely.
#     """
#     with open(json_path, "r") as f:
#         data = json.load(f)
#     bug_specs = BUG_SPECS
#     for system_name, system_data in data.items():
#         # ExplainFuzz may be a list of runs
#         if isinstance(system_data, list):
#             for run in system_data:
#                 examples = run.get("per_bug_example", {})
#                 per_bug_explicit_sensitive = compute_per_bug_explicite_sensitive_rate(examples,bug_specs)
#                 run["per_bug_explicit_sensitive"] = per_bug_explicit_sensitive
#         else:
#             examples = system_data.get("per_bug_example", {})
#             per_bug_explicit_sensitive = compute_per_bug_explicite_sensitive_rate(examples,bug_specs)
#             system_data["per_bug_explicit_sensitive"] = per_bug_explicit_sensitive
#     # Save updated JSON
#     with open(json_path, "w") as f:
#         json.dump(data, f, indent=4)


# def add_explicit_sensitive_metric_safe(json_path):
#     """
#     Load a JSON results file (per seed), compute the overall 'explicit_sensitive'
#     metric as the mean over 'per_bug_explicit_sensitive', and save it back.
#     Handles empty dictionaries safely.
#     """
#     with open(json_path, "r") as f:
#         data = json.load(f)

#     for system_name, system_data in data.items():
#         # ExplainFuzz may be a list of runs
#         if isinstance(system_data, list):
#             for run in system_data:
#                 values = list(run.get("per_bug_explicit_sensitive", {}).values())
#                 run["explicit_sensitive"] = round(np.mean(values), 2) if values else 0.0
#         else:
#             values = list(system_data.get("per_bug_explicit_sensitive", {}).values())
#             system_data["explicit_sensitive"] = round(np.mean(values), 2) if values else 0.0

#     # Save updated JSON
#     with open(json_path, "w") as f:
#         json.dump(data, f, indent=4)

if __name__ == "__main__":
    scenario=2
    for domain in ["SQL1A","SQL2A","SQL3A","SQL4A","SQL"]:
        file_path = f"data/results/multi_bug_rate/scenario_{scenario}_results_multi_bug_{domain}.json"
        #results= run_eval_multi_bug(file_path = file_path,R=3,domain=domain,scenario=scenario)
        #visualize_multi_bug_results(file_path)
    
    # domain = "SQL4"
    # file_path = f"data/results/bug_rate/analysis_seed_{domain}.json"
    # res = eval_multi_bug_rate_seeds(domain)
    # with open(file_path, "w") as f:
    #     json.dump(res, f, indent=4, default=str)

    #get_final_summary_multi_bug_evaluation()

    # file_path_summary = "data/results/multi_bug_rate/per_bug_results_multi_bug.json"
    # keys=["per_bug_counts_distinct","per_bug_explicit_sensitive"]
    # get_final_summary_multi_bug_evaluation(keys,file_path_summary)

    #vizualize_res("data/results/multi_bug_rate/per_bug_results_multi_bug.json")
    generate_table_per_trigger("data/results/multi_bug_rate/per_bug_results_multi_bug.json")