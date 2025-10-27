from bug_specs import BUG_SPECS
from custom_generator_sql.schema import retrieve_schema
from grammarinator_fuzzing.filter_inputs import measure_multi_bug_rate, measure_multi_bug_rate_from_folder, read_queries_from_file
from main import RESULTS_DIR, get_literal_token_mapping, main_generate_inputs
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase
import math


def eval_multi_bug_rate(source: str, path: str, from_file: bool = False,bug_specs={}, scenario=1,tok_condition=None):
    """
    Evaluate multi-bug rate for a given data source.

    Args:
        source (str): Name of the source (e.g., 'Grammarinator', 'ExplainFuzz', 'Seeds')
        path (str): Path to folder or file
        from_file (bool): Whether to read from a single file or from a folder
    """
    print(f"Evaluating {source}...")

    if from_file:
        print(f"Reading the file : {path}")
        queries = read_queries_from_file(path)
        res = measure_multi_bug_rate(queries,bug_specs,scenario,tok_condition)
    else:
        res = measure_multi_bug_rate_from_folder(path,bug_specs,scenario)

    return res


# Convenience wrappers for readability
def eval_multi_bug_rate_Grammarinator(scenario,folder_path):
    return eval_multi_bug_rate(
        source="Grammarinator",
        path=folder_path,
        from_file=False,
        bug_specs=BUG_SPECS,
         scenario=scenario
    )

def eval_multi_bug_rate_ExplainFuzz(domain,scenario,tok_condition=None):
    return eval_multi_bug_rate(
        source="ExplainFuzz",
        path=f"data/output/inputs/{domain}/inputs_no_generate.txt",
        from_file=True,
        bug_specs=BUG_SPECS,
         scenario=scenario,
         tok_condition=tok_condition
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
    res_grammarinator = run_eval_Grammarinator(domain)
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

def run_eval_Grammarinator(domain,res_file_path=None):
    with open(res_file_path, "r") as f:
        results = json.load(f)

    scenario = 2
    results_gram = []
    for try_id in range(3,4):
        folder_path = f"data/intermediate/fuzz_outputs/{domain}/try-{try_id}/no-generate/"
        res_gramm = eval_multi_bug_rate_Grammarinator(scenario,folder_path)
        results_gram.append(res_gramm)
    
    # return results_gram
    
    results["Grammarinator"].append(results_gram)
    

    with open(res_file_path, "w") as f:
        json.dump(results, f, indent=4, default=str)

def run_eval_conditioning(domain,res_file_path,save_file_path,nb_inputs=10000,R=3):
    all_res={}
    with open(res_file_path, "r") as f:
        all_res = json.load(f)
    literal_to_tokens = get_literal_token_mapping(domain)
    results_conditioning=[]
    tokens_covered = set()
    
    conninfo = "dbname=testdb user=bloblo password=bloblotest host=127.0.0.1 port=5432"
    schema = retrieve_schema(conninfo)

    for _,bug_info in BUG_SPECS.items():
        required_tokens = bug_info["required"]
        lit_condition = required_tokens[0] if required_tokens else None
        tok_condition = literal_to_tokens.get(lit_condition,None)
        if tok_condition in tokens_covered:
            continue
       
        results_one_condition=[]
        for _ in range(R):
            print(f"Evaluating conditioning for tok condition {tok_condition}...")
            main_generate_inputs(
                domain=domain,
                mode="no-generate",
                nb_concrete_inputs=nb_inputs,
                token_condition=tok_condition,
                dry_run=True,
                schema=schema
            )
            res_conditioned = eval_multi_bug_rate_ExplainFuzz(domain,scenario=2,tok_condition=lit_condition)
            res_conditioned["conditioning_token"] = lit_condition
            results_one_condition.append(res_conditioned)
            tokens_covered.add(tok_condition)
        results_conditioning.append(results_one_condition)
        
    
    all_res["ExplainFuzz + conditioning"] = results_conditioning
    with open(save_file_path, "w") as f:
        json.dump(all_res, f, indent=4)
    
    return all_res



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
            agg[key] = {}
            for bug in bug_ids:
                vals = [run.get(key,{}).get(bug, 0) for run in seed_results]
                agg[key][bug] = {
                    "mean": np.mean(vals),
                    "std": np.std(vals)
                }
        elif isinstance(seed_results[0][key], str):
            # String metric, keep the first one
            agg[key] = seed_results[0][key]
        else:
            # Scalar metric
            # print([run for run in seed_results])
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
        res_grammarinator = aggregate_results_per_seed(results["Grammarinator"],keys)
        res_explainfuzz = aggregate_results_per_seed(results["ExplainFuzz"],keys)
        final_summary[domain]={"Grammarinator":res_grammarinator,"ExplainFuzz":res_explainfuzz}

    # file_path_summary = "data/results/multi_bug_rate/summary_results_multi_bug.json"
    with open(file_path_summary, "w") as f:
        json.dump(final_summary, f, indent=4, default=str)

def get_final_summary_conditioning_evaluation(keys,file_path_summary):
    final_summary={}
    for domain in ["SQL1A","SQL2A","SQL3A","SQL4A"]:
        file_path = f"data/results/multi_bug_rate/results_multi_bug_{domain}_with_conditioning_fix.json"
        with open(file_path, "r") as f:
            results = json.load(f)
        res_grammarinator = aggregate_results_per_seed(results["Grammarinator"],keys)
        res_explainfuzz = aggregate_results_per_seed(results["ExplainFuzz"],keys)
        summary_domain = {"Grammarinator":res_grammarinator,"ExplainFuzz":res_explainfuzz}
        summary_domain = update_summary_with_conditioning_results(results["ExplainFuzz + conditioning"],keys,summary_domain)

        final_summary[domain]=summary_domain

    # file_path_summary = "data/results/multi_bug_rate/summary_results_multi_bug.json"
    with open(file_path_summary, "w") as f:
        json.dump(final_summary, f, indent=4, default=str)


def update_summary_with_conditioning_results(conditioning_results,keys,summary_domain):
    for cond_res in conditioning_results:
        aggregated_cond_res = aggregate_results_per_seed(cond_res,keys+["conditioning_token"])
        lit_condition = aggregated_cond_res.get("conditioning_token",None)
        method_key = f"ExplainFuzz + {lit_condition}"
        summary_domain[method_key] = aggregated_cond_res
    return summary_domain


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
        plot_per_bug_bar(gramm_data, ef_data, bug_specs=BUG_SPECS, metric=f"per_bug_counts_distinct")

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
                if model == "ExplainFuzz" or model =="Grammarinator":
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

def collect_conditioning_results_bug_level_to_dataframe(file_path, domain):
    with open(file_path, "r") as f:
        summary = json.load(f)

    domain_data = summary[domain]
    rows = []
    exec_rate_rows = []

    all_model_conditionings = set()
    all_bug_ids = set()

    for method_name, data in domain_data.items():
        # Extract conditioning token
        if " + " in method_name:
            model = "ExplainFuzz"
            conditioning = method_name.split(" + ")[-1]
        else:
            model = method_name
            conditioning = "None"
        all_model_conditionings.add((model, conditioning))

        exec_rate_data = data.get("executable_rate", {})
        exec_rate = exec_rate_data.get("mean", 0) if isinstance(exec_rate_data, dict) else exec_rate_data
        exec_rate_rows.append({
            "bug_id": "Execution rate",  # This will appear as a header row
            "model": model,
            "conditioning": conditioning,
            "distinct_queries": round(exec_rate,2) # Convert to percentage if in [0,1]
        })

        per_bug = data.get("per_bug_counts_distinct", {})
        if not per_bug:
            # No bugs triggered at all → keep placeholder zeros later
            continue
        # Handle cases where values might be {bug: {"mean": val, "std": ...}}
        per_bug = {b: (v["mean"] if isinstance(v, dict) and "mean" in v else v)
                   for b, v in per_bug.items()}

        for bug, val in per_bug.items():
            all_bug_ids.add(bug)
            rows.append({
                "bug_id": bug,
                "model": model,
                "conditioning": conditioning,
                "distinct_queries": val
            })


    df = pd.DataFrame(rows+exec_rate_rows)
    if df.empty:
        return pd.DataFrame(columns=pd.MultiIndex.from_tuples(sorted(all_model_conditionings)))

    # Pivot: rows = bugs, columns = model + conditioning
    pivot = df.pivot_table(
        index="bug_id",
        columns=["model", "conditioning"],
        values="distinct_queries",
        fill_value=0,
        aggfunc="mean"
    )

    # ---- Ensure all models and bugs are represented ----
    pivot = pivot.reindex(columns=pd.MultiIndex.from_tuples(sorted(all_model_conditionings)), fill_value=0)
    ordered_bugs = ["Execution rate"] + sorted(all_bug_ids)
    pivot = pivot.reindex(index=ordered_bugs, fill_value=0)

    # ---- Column ordering ----
    desired_order = [("Grammarinator", "None"), ("ExplainFuzz", "None")]
    others = sorted([m for m in pivot.columns if m not in desired_order])
    pivot = pivot[desired_order + others]
    return pivot

import re

def generate_bug_level_table(file_path, domain):
    """
    Generate a LaTeX table showing distinct queries per bug for each model and conditioning.

    Args:
        file_path (str): Path to the detailed JSON result file (with per_bug_counts_distinct)
        domain (str): Domain name, e.g. 'SQL1A'

    Returns:
        pd.DataFrame: the pivoted DataFrame used to generate the table
    """
    pivot = collect_conditioning_results_bug_level_to_dataframe(file_path, domain)

    # Flatten multiindex columns
    pivot.columns = [
        f"{m}" if c == "None" else f"{m}+{c}"
        for (m, c) in pivot.columns
    ]

    # Format the content (bold max values, add % for execution rate)
    formatted = pivot.copy()
    for idx, row in pivot.iterrows():
        max_val = row.max()
        for col in pivot.columns:
            val = row[col]
            if idx == "Execution rate":
                formatted.loc[idx, col] = f"{val:.2f}\\%"
            else:
                formatted.loc[idx, col] = (
                    f"\\textbf{{{val:.0f}}}" if val == max_val and max_val > 0 else f"{val:.0f}"
                )

    # Escape underscores in bug_id names and bold the "Execution rate"
    formatted.index = [
        "\\textbf{Execution rate}" if idx == "Execution rate" else idx.replace("_", "\\_")
        for idx in formatted.index
    ]

    # --- Convert DataFrame to plain LaTeX lines (no headers, no extra environment) ---
    body = formatted.to_latex(
        index=True,
        header=False,
        escape=False,
        column_format="l" + "c" * len(pivot.columns)
    )

    # --- Clean out any tabular or booktabs leftovers from Pandas ---
    lines = []
    for line in body.splitlines():
        if any(skip in line for skip in [
            "\\begin{tabular", "\\end{tabular}", "\\toprule", "\\midrule", "\\bottomrule"
        ]):
            continue
        line = line.strip()
        if line:  # skip empty lines
            lines.append(line)
    body = "\n".join(lines)

    body = re.sub(
    r"(\\textbf\{Execution rate\}.*?\\\\)",
    r"\1\n\\cmidrule(lr){1-" + str(len(pivot.columns) + 1) + "}",
    body,
    flags=re.DOTALL
)

    # --- Build custom LaTeX table with your preferred header ---
    header = (
        "\\toprule\n"
        "  bug\\_id & Gram & EF & "
        "\\shortstack{EF + \\\\GROUP} & "
        "\\shortstack{EF + \\\\JOIN} & "
        "\\shortstack{EF + \\\\NOT} & "
        "\\shortstack{EF + \\\\ORDER} & "
        "\\shortstack{EF + \\\\SELECT} & "
        "\\shortstack{EF + \\\\UNION} & "
        "\\shortstack{EF + \\\\WHERE} \\\\\n"
        "\\midrule\n"
    )

    # Combine everything cleanly
    latex = (
        f"\\begin{{tabular}}{{{'l' + 'c' * len(pivot.columns)}}}\n"
        f"{header}"
        f"{body}\n"
        "\\bottomrule\n"
        "\\end{tabular}"
    )

    print(latex)
    return pivot


def plot_bug_level_heatmap_with_exec(file_path, domain):
    """
    Heatmap with 'Execution rate' as first row.
    - Execution rate uses a blue color scale.
    - Other rows use a green-red scale normalized per row.
    - 'Execution rate' index is bold.
    """
    pivot = collect_conditioning_results_bug_level_to_dataframe(file_path, domain)

    # Separate execution rate row if present
    has_exec = "Execution rate" in pivot.index
    if has_exec:
        exec_row = pivot.loc[["Execution rate"]]
        data = pivot.drop(index="Execution rate")
    else:
        exec_row = None
        data = pivot

    # Normalize bug rows individually (so each bug’s color reflects relative counts)
    norm_data = data.div(data.max(axis=1), axis=0).fillna(0)

    # Combine execution rate (0–100%) at the top
    if exec_row is not None:
        combined = pd.concat([exec_row / 100.0, norm_data])
    else:
        combined = norm_data

    # Prepare annotations
    ann = combined.copy().astype(str)  # 👈 ensures dtype is object (string)
    if exec_row is not None:
        ann.loc["Execution rate"] = [f"{v:.1f}%" for v in exec_row.loc["Execution rate"]]
    for idx in data.index:
        ann.loc[idx] = data.loc[idx].apply(lambda x: f"{math.ceil(x):d}")
        

    # Create figure
    plt.figure(figsize=(12, max(6, len(combined) * 0.4)))

    # Plot main heatmap (green-red)
    ax = sns.heatmap(
        combined,
        annot=ann,
        fmt="",
        cmap="RdYlGn",
        cbar=False,
        vmin=0,
        vmax=1,
        linewidths=0.5
    )
    
    # Overlay a blue colormap only on the execution rate row (if present)
    if has_exec:
        y0 = 0  # top row in heatmap (matplotlib flips y-axis)
        blue_cmap = plt.cm.Blues
        for j, val in enumerate(exec_row.iloc[0] / 100.0):
            color = blue_cmap(val)
            ax.add_patch(plt.Rectangle((j, y0), 1, 1, color=color, ec='none', lw=0))
        for text in ax.texts:
            if abs(text.get_position()[1] - (y0 + 0.5)) < 0.1:  # text centered in that row
                text.set_color("black")

    yticks = ax.get_yticklabels()
    new_labels = []
    for tick in yticks:
        text = tick.get_text()
        if text == "Execution rate":
            new_labels.append(r"$\bf{Execution\ Rate}$")  # bold label using mathtext
        else:
            new_labels.append(text)
    ax.set_yticklabels(new_labels, rotation=0, fontsize=9)

    new_labels_models= []
    for tick in ax.get_xticklabels():
        text = tick.get_text()
        if "None" in text:
            text = text.replace("-None","")
        new_labels_models.append(text)
    ax.set_xticklabels(new_labels_models, rotation=30, ha='right', fontsize=9)

    # --- Add colorbars manually ---
    # 1️⃣ Green-red bar for Distinct Queries
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)
    cax1 = divider.append_axes("right", size="3%", pad=0.05)
    norm_green = Normalize(vmin=0, vmax=1)
    cb1 = ColorbarBase(cax1, cmap=plt.cm.RdYlGn, norm=norm_green)
    cb1.set_label("Distinct Queries (normalized)")

    # 2️⃣ Blue bar for Execution Rate
    if has_exec:
        cax2 = divider.append_axes("right", size="3%", pad=0.7)
        norm_blue = Normalize(vmin=0, vmax=100)
        cb2 = ColorbarBase(cax2, cmap=plt.cm.Blues, norm=norm_blue)
        cb2.set_label("Execution Rate (%)")

    # Title and layout
    ax.set_title(f"Bug-Level Distinct Queries ({domain[:-1]})", fontsize=14)
    ax.set_xlabel("Model + Conditioning")
    ax.set_ylabel("")
    
    plt.tight_layout()
    plt.show()


def generate_table_summary_results_multi_bug(file_path_summary):
    # --- Load your JSON file ---
    with open(file_path_summary, "r") as f:
        data = json.load(f)

    # --- Column order and formatting ---
    metrics = [
        ("executable_rate", "Executable (\\%)"),
        ("nb_distinct_bugs_triggered", "\\# Bugs"),
        ("coverage", "Coverage (\\%)"),
        ("total_triggers", "Total triggers"),
        ("total_distinct_queries", "Total distinct queries"),
        ("avg_distinct_per_bug", "Avg distinct / bug"),
        ("explicit_sensitive", "Explicit sensitive (\\%)")
    ]

    # --- Generate LaTeX table ---
    latex_lines = []
    latex_lines.append("\\begin{tabular}{l l r r r r r r r}")
    latex_lines.append("\\toprule")
    header = "Seed & System & " + " & ".join([label for _, label in metrics]) + " \\\\"
    latex_lines.append(header)
    latex_lines.append("\\midrule")

    for i, (domain, systems) in enumerate(data.items()):
        # Example: domain = "SQL1A" → Seed = SQL-1
        seed_label = domain.replace("A", "").replace("SQL", "SQL-")

        # First system: Grammarinator
        gramm = systems.get("Grammarinator", {})
        expl = systems.get("ExplainFuzz", {})

        def fmt(m):
            mean = gramm[m]["mean"]
            std = gramm[m]["std"]
            return f"{mean:.2f} $\\pm$ {std:.2f}"

        row_gramm = " & ".join([fmt(m) for m, _ in metrics])

        def fmt2(m):
            mean = expl[m]["mean"]
            std = expl[m]["std"]
            return f"{mean:.2f} $\\pm$ {std:.2f}"

        row_expl = " & ".join([fmt2(m) for m, _ in metrics])

        latex_lines.append(f"\\multirow{{2}}{{*}}{{{seed_label}}} ")
        latex_lines.append(f"& Grammarinator & {row_gramm} \\\\")
        latex_lines.append(f"& ExplainFuzz & {row_expl} \\\\")

        # Add midrule between seeds
        if i < len(data) - 1:
            latex_lines.append("\\midrule")

    latex_lines.append("\\bottomrule")
    latex_lines.append("\\end{tabular}")

    # --- Print or save the LaTeX table ---
    latex_table = "\n".join(latex_lines)
    print(latex_table)

if __name__ == "__main__":
    # scenario=2
    # for domain in ["SQL1A","SQL2A","SQL3A","SQL4A","SQL"]:
    # domain = "SQL2A"
    # file_path = f"data/results/multi_bug_rate/scenario_{scenario}_results_multi_bug_{domain}.json"
    # results= run_eval_multi_bug(file_path = file_path,R=3,domain=domain,scenario=scenario)
    # visualize_multi_bug_results(file_path)
    
    # domain = "SQL4"
    # file_path = f"data/results/bug_rate/analysis_seed_{domain}.json"
    # res = eval_multi_bug_rate_seeds(domain)
    # with open(file_path, "w") as f:
    #     json.dump(res, f, indent=4, default=str)
    
    ## Generating the summary file
    keys = ["executable_rate", "nb_distinct_bugs_triggered", "coverage",
            "total_triggers", "total_distinct_queries", 
            "avg_inputs_per_bug", "avg_distinct_per_bug","explicit_sensitive","per_bug_counts_distinct"]
    # file_path_summary = "data/results/multi_bug_rate/summary_results_multi_bug.json"
    
    # get_final_summary_multi_bug_evaluation(keys,file_path_summary)
    file_path_summary_conditioning = "data/results/multi_bug_rate/summary_results_multi_bug_with_conditioning_fix.json"
    #get_final_summary_conditioning_evaluation(keys, file_path_summary_conditioning)
    # for domain in ["SQL1A","SQL2A","SQL3A","SQL4A"]:
    #domain = "SQL3A"
    # generate_bug_level_table(file_path_summary_conditioning, domain)
    #plot_bug_level_heatmap_with_exec(file_path_summary_conditioning, domain)
        # plot_execution_rate_heatmap(file_path_summary_conditioning, domain)
    
    ## Generate the summary file for the different bugs
    # file_path_summary = "data/results/multi_bug_rate/per_bug_results_multi_bug.json"
    # keys=["per_bug_counts_distinct","per_bug_explicit_sensitive"]
    # get_final_summary_multi_bug_evaluation(keys,file_path_summary)

    #vizualize_res("data/results/multi_bug_rate/per_bug_results_multi_bug.json")
    # generate_table_per_trigger("data/results/multi_bug_rate/per_bug_results_multi_bug.json")

    # for domain in ["SQL1A"]:
    #     print(f"Evaluation for the domain {domain}")
    #     run_eval_Grammarinator(domain,f"data/results/multi_bug_rate/scenario_2_results_multi_bug_{domain}.json") # Looks good
    # 

    # RUNNING CONDITIONING EVALUATION
    # for domain in ["SQL1A","SQL2A","SQL3A","SQL4A"]:
    #     all_res = run_eval_conditioning(
    #         domain,
    #         f"data/results/multi_bug_rate/scenario_2_results_multi_bug_{domain}.json",
    #         f"data/results/multi_bug_rate/results_multi_bug_{domain}_with_conditioning_fix.json",
    #         nb_inputs=10000,
    #         R=3
    #     )

    # ## Running the evaluations for the domain SQL4A
    # scenario=2
    # domain = "SQL4A"
    # file_path = f"data/results/multi_bug_rate/scenario_{scenario}_results_multi_bug_{domain}.json"
    # results= run_eval_multi_bug(file_path = file_path,R=3,domain=domain,scenario=scenario)
    # all_res = run_eval_conditioning(
    #         domain,
    #         f"data/results/multi_bug_rate/scenario_2_results_multi_bug_{domain}.json",
    #         f"data/results/multi_bug_rate/results_multi_bug_{domain}_with_conditioning_fix.json",
    #         nb_inputs=10000,
    #         R=3
    #     )
    
    ## Generate summary files
    domain = "SQL4A"
    print("Generating summary file multi bug ")
    keys = ["executable_rate", "nb_distinct_bugs_triggered", "coverage",
            "total_triggers", "total_distinct_queries", 
            "avg_inputs_per_bug", "avg_distinct_per_bug","explicit_sensitive"]
    file_path_summary = "data/results/multi_bug_rate/summary_results_multi_bug.json"
    get_final_summary_multi_bug_evaluation(keys,file_path_summary)
    
    print("Generating summary conditioning")
    keys = ["executable_rate", "nb_distinct_bugs_triggered", "coverage",
            "total_triggers", "total_distinct_queries", 
            "avg_inputs_per_bug", "avg_distinct_per_bug","explicit_sensitive","per_bug_counts_distinct"]
    file_path_summary_conditioning = "data/results/multi_bug_rate/summary_results_multi_bug_with_conditioning_fix.json"
    get_final_summary_conditioning_evaluation(keys, file_path_summary_conditioning)

    print("Generating summary per bug ")
    file_path_summary_per_bug = "data/results/multi_bug_rate/per_bug_results_multi_bug.json"
    keys_per_bug=["per_bug_counts_distinct","per_bug_explicit_sensitive"]
    get_final_summary_multi_bug_evaluation(keys_per_bug,file_path_summary_per_bug)


    ## Visualize results

    # Results with conditioning
    # generate_bug_level_table(file_path_summary_conditioning, domain)
    plot_bug_level_heatmap_with_exec(file_path_summary_conditioning, domain)

    # Results per bug
    #vizualize_res("data/results/multi_bug_rate/per_bug_results_multi_bug.json")
    # generate_table_per_trigger("data/results/multi_bug_rate/per_bug_results_multi_bug.json")

    # generate_table_summary_results_multi_bug(file_path_summary)
    

    # run_eval_Grammarinator("SQL4A",f"data/results/multi_bug_rate/scenario_2_results_multi_bug_SQL4A.json")