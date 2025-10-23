import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import math



def get_df_domain(domain, results_path):
    # Load the results
    with open(results_path, "r") as file:
        data = json.load(file)

    # Convert to DataFrame
    df = pd.DataFrame(data[domain])
    return df


def analyze_results_PC(domain, results_file):
    df = get_df_domain(domain, results_file)

    # Ensure types are consistent
    df["last-training-loss"] = df["last-training-loss"].astype(float)
    df["avg-loglikelihood"] = df["avg-loglikelihood"].astype(float)
    df["train_time"] = df["train_time"].astype(float)

    # Plot avg-loglikelihood vs max_length, separately for each mode
    sns.lineplot(data=df, x="max_length", y="avg-loglikelihood", hue="mode", marker="o")
    plt.title(f"Length Generalization: Log-likelihood vs Max Length ({domain})")
    plt.xlabel("Max Length")
    plt.ylabel("Avg Log-Likelihood")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="max_length", y="nb_training_queries", hue="mode", alpha=0.8)
    plt.title(f"Number of Training Queries per Max Length ({domain})")
    plt.xlabel("Max Length")
    plt.ylabel("Number of Training Queries")
    plt.legend(title="Mode")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

    # Bar plot: avg-loglikelihood for generate vs no-generate
    sns.barplot(data=df, x="mode", y="avg-loglikelihood", errorbar=None)
    plt.title(f"Compare Modes: Avg Log-Likelihood ({domain})")
    plt.xlabel("Mode")
    plt.ylabel("Avg Log-Likelihood")
    plt.grid(True)
    plt.show()

    # Plot train_time vs max_length
    sns.lineplot(data=df, x="max_length", y="train_time", hue="mode", marker="o")
    plt.title(f"Efficiency: Time vs Max Length ({domain})")
    plt.xlabel("Max Length")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 2. circuit_size vs nb_training_queries
    sns.lineplot(
        data=df, x="nb_training_queries", y="train_time", hue="mode", style="mode"
    )
    plt.title(f"Training Queries vs Train time ({domain})")
    plt.xlabel("Number of Training Queries ")
    plt.ylabel("Train Time (s)")
    plt.grid(True)
    plt.show()

    # 3. Pearson Correlations grouped by mode
    grouped_corr = (
        df.groupby("mode")[["circuit_size", "train_time", "nb_training_queries"]]
        .corr()
        .unstack()
        .iloc[:, 1]
    )
    print("\nCorrelation matrix (Pearson) per mode:")
    print(grouped_corr)

    # Circuit_size vs max_length
    sns.lineplot(data=df, x="max_length", y="circuit_size")
    plt.title(f"Circuit Size VS Max length ({domain})")
    plt.xlabel("Max length")
    plt.ylabel("Circuit Size")
    plt.grid(True)
    plt.show()


def analyze_results_PCFG(domain, results_file):
    df = get_df_domain(domain, results_file)

    # Log-likelihood VS max_length
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x="max_length", y="avg-loglikelihood", hue="mode", marker="o")
    plt.title("Avg Log-Likelihood vs Max Length")
    plt.xlabel("Max Length")
    plt.ylabel("Average Log-Likelihood")
    plt.tight_layout()
    plt.show()


def compare_results_model(
    domain,
    results_PC_file,
    results_PCFG_file,
    results_LLM_file,
    results_seeds_file,
    results_PC_HMM_file=None,
):
    df_PC = get_df_domain(domain, results_PC_file)
    df_PC["method"] = "PC (ExplainFuzz)"
    df_PCFG = get_df_domain(domain, results_PCFG_file)
    # df_LLM = get_df_domain(domain, results_LLM_file)
    if results_PC_HMM_file:
        df_PC_HMM = get_df_domain(domain, results_PC_HMM_file)
    df_seeds = get_df_domain(domain, results_seeds_file)
    if results_PC_HMM_file:
        df = pd.concat([df_PC, df_PCFG, df_PC_HMM], ignore_index=True)
    else:
        df = pd.concat([df_PC, df_PCFG], ignore_index=True)

    # --- Plot 1: Log-Likelihood vs Max Length ---

    def adjust_lightness(color, factor):
        """Lighten or darken a color by multiplying (factor <1 = darker, >1 = lighter)."""
        r, g, b = to_rgb(color)
        return (min(r * factor, 1), min(g * factor, 1), min(b * factor, 1))

    # Define base colors for each method
    palette = sns.color_palette()
    colors = {
        "PC (ExplainFuzz)": palette[0],
        "PCFG": palette[1],
        "LLM": palette[2],
        "PC (HMM)": palette[3],
    }

    # Create custom palette for method + mode
    custom_palette = {}
    for method in colors:
        base = colors[method]
        custom_palette[f"{method} / with-generate"] = adjust_lightness(base, 1.3)
        custom_palette[f"{method} / no-generate"] = adjust_lightness(base, 0.8)

    # Create method/mode label
    df["method_mode"] = df["method"] + " / " + df.get("mode", "")
    df_filtered = df[df["mode"] == "no-generate"]
    df_filtered = df_filtered[df["max_length"]>=15]

    # # Plot
    # plt.figure(figsize=(12, 6))
    # sns.barplot(
    #     data=df,
    #     x="max_length",
    #     y="avg-loglikelihood",
    #     hue="method_mode",
    #     palette=custom_palette,
    #     dodge=True,
    # )

    # plt.title("Log-Likelihood vs Max Length (by Method and Mode)")
    # plt.xlabel("Max Length")
    # plt.ylabel("Average Log-Likelihood")
    # plt.legend(title="Method / Mode", bbox_to_anchor=(1.05, 1), loc="upper left")
    # plt.tight_layout()
    # plt.show()

    # line chart
    # plt.figure(figsize=(10, 6))
    # sns.lineplot(
    #     data=df_filtered,
    #     x="max_length",
    #     y="avg-loglikelihood",
    #     hue="method",
    #     marker="o",
    # )
    # plt.title(f"Negative Log-Likelihood vs Max Length ({domain})")
    # plt.xlabel("Max Length", fontsize=16)
    # plt.ylabel("Negative Log-Likelihood", fontsize=14)
    # plt.legend(title="Method", title_fontsize=14, fontsize=14)
    # plt.xticks(fontsize=14)
    # plt.tight_layout()
    # plt.show()

    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df_filtered,
        x="max_length",
        y="perplexity",
        hue="method",
        marker="o",
        palette=colors
    )
    plt.title(f"Perplexity vs Max Length ({domain})")
    plt.xlabel("Max Length", fontsize=16)
    plt.ylabel("Perplexity", fontsize=14)
    plt.legend(title="Method", title_fontsize=14, fontsize=14)
    plt.xticks([15, 20, 25, 30, 35], fontsize=14)
    plt.tight_layout()
    # plt.yscale("log")
    plt.show()

    # With the average seed length

    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df_filtered,
        x="max_length",
        y="avg-loglikelihood",
        hue="method",
        marker="o",
    )

    # Add a star marker for each method at avg_seeds_length
    for method in df_filtered["method"].unique():
        x_star = (
            int(df_seeds["avg_sequence_length"]) // 5 * 5
        )  # round down to nearest 5
        # Filter for the specific method and x_star
        subset = df_filtered[
            (df_filtered["method"] == method) & (df_filtered["max_length"] == x_star)
        ]

        if not subset.empty:
            y_star = subset["avg-loglikelihood"].values[0]
            plt.scatter(
                x_star,
                y_star,
                marker="*",
                s=150,
                color="black",
                label=f"{method} @ avg seed length",
            )

    # Avoid duplicating legends
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), title="Method / Mode")

    plt.title(f"Log-Likelihood vs Max Length ({domain})")
    plt.xlabel("Max Length")
    plt.ylabel("Average Log-Likelihood")
    plt.tight_layout()
    plt.show()


# --- Plot 2: Log-Likelihood vs Query Type (mode) ---
# plt.figure(figsize=(8, 6))
# sns.barplot(data=df, x="mode", y="avg-loglikelihood", hue="method", errorbar="sd")
# plt.title(f"Log-Likelihood vs Query Type ({domain})")
# plt.xlabel("Query Type")
# plt.ylabel("Average Log-Likelihood")
# plt.tight_layout()
# plt.show()


def comparison_likelihood_domains(
    domains, results_PC_file, results_PCFG_file, results_LLM_file
):
    all_data = []

    for domain in domains:
        df_PC = get_df_domain(domain, results_PC_file)
        df_PCFG = get_df_domain(domain, results_PCFG_file)
        df_LLM = get_df_domain(domain, results_LLM_file)

        all_data.append(pd.concat([df_PC, df_PCFG, df_LLM], ignore_index=True))

    # Combine all domains' data
    df_all = pd.concat(all_data, ignore_index=True)

    # Filter to only 'no-generate' mode
    df_filtered = df_all[df_all["mode"] == "no-generate"]

    # Plot: Domain on X-axis, avg-loglikelihood as bars, grouped by method
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df_filtered,
        x="domain",
        y="avg-loglikelihood",
        hue="method",
        errorbar="sd",
    )
    print(sns.color_palette())
    plt.title("Average Log-Likelihood (no-generate) Across Domains")
    plt.xlabel("Domain")
    plt.ylabel("Average Log-Likelihood")
    plt.tight_layout()
    plt.legend(title="Method")
    plt.show()

def comparison_perplexity_domains_with_HMM_only_realistic_data(
    domains,
    results_PC_file,
    results_PCFG_file,
    results_LLM_file,
    results_PC_HMM_file,
    seeds_info_file,
    use_computed_realistic=True,  # if False, uses "realistic_max_length" instead
):
    """
    Compare perplexity across domains for the realistic max length only.

    Args:
        domains: list of domain names.
        results_*_file: JSON or CSV paths for each model (loaded by get_df_domain()).
        seeds_info_file: path to JSON containing per-domain realistic lengths.
        use_computed_realistic: whether to use "computed_realistic_snapped" (True)
                                or "realistic_max_length" (False).
    """
    import json

    # --- Load seeds info
    with open(seeds_info_file, "r") as f:
        seeds_data = json.load(f)

    # Extract mapping domain -> realistic length
    realistic_map = {}
    for domain, entries in seeds_data.items():
        if not entries:
            continue
        # If multiple entries, pick the first (or we could average, but you can change this)
        # val = (
        #     entries[0].get("computed_realistic_max_length")
        #     if use_computed_realistic
        #     else entries[0].get("realistic_max_length")
        # )

        val = (
            entries[0].get("maximum_max_length_available")
            if use_computed_realistic
            else entries[0].get("realistic_max_length")
        )
        realistic_map[domain] = int(val) if val is not None else None
    # --- Gather all results
    all_data = []

    for domain in domains:
        df_PC = get_df_domain(domain, results_PC_file)
        df_PC["method"] = "PC (ExplainFuzz)"
        df_PCFG = get_df_domain(domain, results_PCFG_file)
        df_PCFG["method"] = "PCFG"
        df_PC_HMM = get_df_domain(domain, results_PC_HMM_file)
        df_PC_HMM["method"] = "PC (HMM)"

        # If you later re-add LLM results
        df_LLM = get_df_domain(domain, results_LLM_file)
        df_LLM["method"] = "LLM"

        # Concatenate all models for this domain
        df_domain_all = pd.concat([df_PC, df_PC_HMM, df_PCFG,df_LLM], ignore_index=True)

        # --- Filter by realistic max length
        realistic_len = realistic_map.get(domain)
        if realistic_len is not None:
            df_domain_all = df_domain_all[df_domain_all["max_length"] == realistic_len]
        else:
            print(f"⚠️ No realistic max length found for {domain}, keeping all lengths.")

        all_data.append(df_domain_all)

    # --- Combine all domains
    df_all = pd.concat(all_data, ignore_index=True)

    # --- Keep only 'no-generate' mode
    df_filtered = df_all[df_all["mode"] == "no-generate"]

    print(df_filtered["method"])

    # --- Debug info
    print("\nPerplexity summary:")
    print(df_filtered["perplexity"].describe())
    print("\nFiltered data sample:")
    print(df_filtered.head())

    # --- Plot
    palette = sns.color_palette()
    colors = {
        "PC (ExplainFuzz)": palette[0],
        "PCFG": palette[1],
        "LLM": palette[2],
        "PC (HMM)": palette[3],
    }

    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=df_filtered,
        x="domain",
        y="perplexity",
        hue="method",
        errorbar="sd",
        palette=colors,
    )
    plt.title("Perplexity Across Domains", fontsize=18)
    plt.xlabel("Domain", fontsize=18)
    plt.ylabel("Perplexity", fontsize=18)
    plt.xticks(fontsize=16)
    plt.tight_layout()
    plt.legend(title="Method", title_fontsize=14, fontsize=14)
    # plt.show()

    return df_filtered


def df_filtered_to_latex_table(df_filtered, caption="Perplexity per Domain (Maximum Length available)", label="tab:perplexity"):
    """
    Convert a filtered DataFrame (one entry per domain-method) to a LaTeX table.

    Parameters:
    - df_filtered: DataFrame with columns ['domain', 'method', 'perplexity']
    - caption: Table caption
    - label: LaTeX label

    Returns:
    - LaTeX table as a string
    """

    # Pivot the perplexity table
    pivot = df_filtered.pivot(index="domain", columns="method", values="perplexity").round(2)
    pivot = pivot.applymap(lambda x: f"{x:.2f}")

    # Reorder methods
    methods_order = ["LLM", "PCFG", "PC (HMM)", "PC (ExplainFuzz)"]
    pivot = pivot[[m for m in methods_order if m in pivot.columns]]

    # Add max_length column (just take first value per domain)
    max_length_per_domain = df_filtered.groupby("domain")["max_length"].first()
    pivot["max_length"] = pivot.index.map(max_length_per_domain)

    # Bold the best (lowest) perplexity per domain
    for domain in pivot.index:
        row = pivot.loc[domain, methods_order]  # only method columns
        best_method = row.astype(float).idxmin()
        pivot.loc[domain, best_method] = f"\\textbf{{{row[best_method]}}}"

    # Optionally, move max_length to the first column
    pivot = pivot[["max_length"] + [m for m in methods_order if m in pivot.columns]]

    # Generate LaTeX code
    latex_table = pivot.to_latex(
        escape=False,
        caption=caption,
        label=label,
        column_format="l" + "c" * len(pivot.columns),
        multicolumn=True,
        multicolumn_format="c",
)
    return latex_table

def comparison_perplexity_domains_with_HMM(
    domains, results_PC_file, results_PCFG_file, results_LLM_file, results_PC_HMM_file
):
    all_data = []

    for domain in domains:
        df_PC = get_df_domain(domain, results_PC_file)
        df_PC["method"] = "PC (ExplainFuzz)"
        df_PCFG = get_df_domain(domain, results_PCFG_file)
        df_LLM = get_df_domain(domain, results_LLM_file)
        df_PC_HMM = get_df_domain(domain, results_PC_HMM_file)

        all_data.append(
            pd.concat([df_PC, df_PC_HMM, df_PCFG], ignore_index=True)
        )

    # Combine all domains' data
    df_all = pd.concat(all_data, ignore_index=True)

    # Filter to only 'no-generate' mode
    df_filtered = df_all[df_all["mode"] == "no-generate"]

    print(df_filtered["perplexity"].describe())
    print(df_filtered)
    palette = sns.color_palette()
    colors = {
        "PC (ExplainFuzz)": palette[0],
        "PCFG": palette[1],
        "LLM": palette[2],
        "PC (HMM)": palette[3],
    }

    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=df_filtered,
        x="domain",
        y="perplexity",
        hue="method",
        errorbar="sd",
        palette=colors,
    )
    plt.title("Average perplexity Across Domains", fontsize=18)
    plt.xlabel("Domain", fontsize=18)
    plt.ylabel("Average perplexity", fontsize=18)
    plt.xticks(fontsize=18)
    plt.tight_layout()
    plt.legend(title="Method", title_fontsize=16, fontsize=16)
    # plt.yscale("log")
    plt.show()


def comparison_likelihood_domains_with_HMM(
    domains, results_PC_file, results_PCFG_file, results_LLM_file, results_PC_HMM_file
):
    all_data = []

    for domain in domains:
        df_PC = get_df_domain(domain, results_PC_file)
        df_PC["method"] = "PC (ExplainFuzz)"
        df_PCFG = get_df_domain(domain, results_PCFG_file)
        # df_LLM = get_df_domain(domain, results_LLM_file)
        df_PC_HMM = get_df_domain(domain, results_PC_HMM_file)

        all_data.append(
            pd.concat([df_PC, df_PC_HMM, df_PCFG], ignore_index=True)
        )

    # Combine all domains' data
    df_all = pd.concat(all_data, ignore_index=True)

    # Filter to only 'no-generate' mode
    df_filtered = df_all[df_all["mode"] == "no-generate"]
    print(df_filtered)
    palette = sns.color_palette()
    colors = {
        "PC (ExplainFuzz)": palette[0],
        "PCFG": palette[1],
        "LLM": palette[2],
        "PC (HMM)": palette[3],
    }

    #Plot: Domain on X-axis, avg-loglikelihood as bars, grouped by method
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df_filtered,
        x="domain",
        y="avg-loglikelihood",
        hue="method",
        errorbar="sd",
        palette=colors,
    )
    plt.title("Average Negative Log-Likelihood Across Domains", fontsize=18)
    plt.xlabel("Domain", fontsize=18)
    plt.ylabel("Average Negative Log-Likelihood", fontsize=18)
    plt.xticks(fontsize=18)
    plt.tight_layout()
    plt.legend(title="Method", title_fontsize=16, fontsize=16)
    plt.show()


def compare_grammar_complexity(domains, results_grammars_file):
    # Load and merge data
    data = []
    for domain in domains:
        df = get_df_domain(domain, results_grammars_file)
        df["nb_recursive_rules"] = df["percent_recursive"] * df["num_productions"]
        data.append(df)

    df_all = pd.concat(data, ignore_index=True)

    # Select and log-transform relevant metrics
    metrics = [
        "num_rules",
        "num_productions",
        "num_terminals",
        "avg_arity",
        "nb_recursive_rules",
    ]
    df_plot = df_all[["domain"] + metrics].copy()
    for m in metrics:
        df_plot[m] = df_plot[m].apply(lambda x: math.log1p(x))  # log(1+x) to handle 0

    # Melt for seaborn plotting
    df_melted = pd.melt(
        df_plot, id_vars=["domain"], var_name="Metric", value_name="Value"
    )

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_melted, x="Value", y="domain", hue="Metric")
    plt.xlabel("Log-Scaled Value")
    plt.ylabel("Domain")
    plt.title("Grammar Complexity Comparison Across Domains")
    plt.tight_layout()
    plt.show()


def plot_seed_lengths(domains, results_seeds_file):
    # Flatten into a DataFrame
    data = []
    for domain in domains:
        df = get_df_domain(domain, results_seeds_file)
        data.append(df)

    df_all = pd.concat(data, ignore_index=True)
    # Select only relevant columns for plotting
    df_plot = df_all[
        ["domain", "min_sequence_length", "max_sequence_length", "avg_sequence_length"]
    ]

    # Rename columns for consistency
    df_plot = df_plot.rename(
        columns={
            "domain": "Domain",
            "min_sequence_length": "Min Length",
            "max_sequence_length": "Max Length",
            "avg_sequence_length": "Avg Length",
        }
    )

    # Melt the dataframe for seaborn
    df_melted = df_plot.melt(id_vars="Domain", var_name="Metric", value_name="Length")

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_melted, x="Domain", y="Length", hue="Metric", palette="muted")
    plt.yscale("log")
    plt.title("Seed Sequence Lengths per Domain (Log Scale)")
    plt.ylabel("Sequence Length (log scale)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title="Metric")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.show()

    df_plot = df_all[["domain", "avg_sequence_length"]]
    df_plot = df_plot.rename(
        columns={
            "domain": "Domain",
            "avg_sequence_length": "Avg Length",
        }
    )
    df_melted = df_plot.melt(id_vars="Domain", var_name="Metric", value_name="Length")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_melted, x="Domain", y="Length", hue="Metric", palette="Set2")
    plt.yscale("log")
    plt.title("Seed Sequence Lengths per Domain (Log Scale)")
    plt.ylabel("Sequence Length (log scale)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title="Metric")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.show()


def compare_circuit_size(domains, results_PC_file):
    data = []
    for domain in domains:
        df = get_df_domain(domain, results_PC_file)
        df = df[df["mode"] == "no-generate"]
        data.append(df)

    df_all = pd.concat(data, ignore_index=True)

    palette = sns.color_palette(n_colors=len(df_all["domain"].unique()))
    domain_colors = dict(zip(df_all["domain"].unique(), palette))

    sns.lineplot(
        data=df_all,
        x="max_length",
        y="circuit_size",
        hue="domain",
        palette=domain_colors,
    )

    # Add stars at average seed length with domain-specific color
    # for domain in df_all["domain"].unique():
    #     df_seed = get_df_domain(domain, results_seeds_file)
    #     x_star = int(df_seed["avg_sequence_length"].iloc[0]) // 5 * 5
    #     subset = df_all[(df_all["domain"] == domain) & (df_all["max_length"] == x_star)]

    #     if not subset.empty:
    #         y_star = subset["circuit_size"].values[0]
    #         plt.scatter(
    #             x_star,
    #             y_star,
    #             marker="*",
    #             s=150,
    #             color=domain_colors[domain],
    #             label="_nolegend_",
    #         )

    # plt.scatter([], [], marker="*", s=150, color="black", label="Avg seed length")
    plt.title("Circuit Size vs Max Length")
    plt.xlabel("Max length")
    plt.ylabel("Circuit Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def compare_compilation_time(domains, results_PC_file, results_seeds_file):
    data = []
    for domain in domains:
        df = get_df_domain(domain, results_PC_file)
        df = df[df["mode"] == "no-generate"]
        data.append(df)

    df_all = pd.concat(data, ignore_index=True)

    palette = sns.color_palette(n_colors=len(df_all["domain"].unique()))
    domain_colors = dict(zip(df_all["domain"].unique(), palette))
    sns.lineplot(data=df_all, x="max_length", y="time_building_circuit", hue="domain")
    # for domain in df_all["domain"].unique():
    #     df_seed = get_df_domain(domain, results_seeds_file)
    #     x_star = int(df_seed["avg_sequence_length"].iloc[0]) // 5 * 5
    #     subset = df_all[(df_all["domain"] == domain) & (df_all["max_length"] == x_star)]

    #     if not subset.empty:
    #         y_star = subset["time_building_circuit"].values[0]
    #         plt.scatter(
    #             x_star,
    #             y_star,
    #             marker="*",
    #             s=150,
    #             color=domain_colors[domain],
    #             label="_nolegend_",
    #         )
    #     elif x_star <= 200:
    #         plt.scatter(
    #             x_star,
    #             0,
    #             marker="*",
    #             s=150,
    #             color=domain_colors[domain],
    #             label="_nolegend_",
    #         )

    # plt.scatter([], [], marker="*", s=150, color="black", label="Avg seed length")

    plt.title(f"Compilation Time VS Max length")
    plt.xlabel("Max length")
    # plt.yscale("log")
    plt.ylabel("Compilation time")
    plt.legend()
    plt.grid(True)
    plt.show()

    sns.lineplot(data=df_all, x="max_length", y="circuit_size", hue="domain")
    plt.title(f"Circuit Size VS Max length")
    plt.xlabel("Max length")
    # plt.yscale("log")
    plt.ylabel("Circuit size")
    plt.legend()
    plt.grid(True)
    plt.show()


def compare_train_time(domains, results_PC_file, results_seeds_file):
    data = []
    data_seed = []
    for domain in domains:
        df = get_df_domain(domain, results_PC_file)
        df = df[df["mode"] == "no-generate"]
        data.append(df)

    df_all = pd.concat(data, ignore_index=True)

    palette = sns.color_palette(n_colors=len(df_all["domain"].unique()))
    domain_colors = dict(zip(df_all["domain"].unique(), palette))

    sns.lineplot(data=df_all, x="max_length", y="train_time", hue="domain")
    for domain in df_all["domain"].unique():
        df_seed = get_df_domain(domain, results_seeds_file)
        x_star = int(df_seed["avg_sequence_length"].iloc[0]) // 5 * 5
        subset = df_all[(df_all["domain"] == domain) & (df_all["max_length"] == x_star)]

        if not subset.empty:
            y_star = subset["train_time"].values[0]
            plt.scatter(
                x_star,
                y_star,
                marker="*",
                s=150,
                color=domain_colors[domain],
                label="_nolegend_",
            )

    plt.scatter([], [], marker="*", s=150, color="black", label="Avg seed length")

    plt.title(f"Training time VS Max length")
    plt.xlabel("Max length")
    plt.ylabel("Training time")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    domain = "SQL"
    # analyze_results_PC(domain, "data/results/PC/eval_PC_model.json")
    # # analyze_results_PCFG(domain, "data/results/PCFG/eval_PCFG_fix_depth.json")

    # compare_results_model(
    #     domain,
    #     "data/results/PC/eval_PC_model.json",
    #     "data/results/PCFG/eval_PCFG.json",
    #     "data/results/LLM/eval_llm.json",
    #     "data/results/SEEDS/eval_seeds.json",
    #     "data/results/PC-HMM/eval_PC_HMM.json",
    # )

    # compare_results_model(
    #     domain,
    #     "data/results/PC/eval_PC_model_with_perplexity_bis.json",
    #     "data/results/PCFG/eval_PCFG_with_perplexity_bis.json",
    #     "data/results/LLM/eval_llm_with_perplexity_bis.json",
    #     "data/results/SEEDS/eval_seeds.json",
    #     "data/results/PC-HMM/eval_PC_HMM_with_perplexity_bis.json",
    # )

    # compare_results_model(domain,
    #      "data/results_october/PC/eval_PC_model.json",
    #     "data/results_october/PCFG/eval_PCFG.json",
    #     "data/results_october/LLM/eval_llm.json",
    #     "data/results/SEEDS/eval_seeds_updated.json",
    #     "data/results/PC-HMM/eval_PC_HMM_with_perplexity_bis.json"
    #     )
    # domains = ["CSV", "HTML"]
    # for domain in domains:
    #     compare_results_model(
    #         domain,
    #         "data/results/PC/eval_PC_model.json",
    #         "data/results/PCFG/eval_PCFG.json",
    #         "data/results/LLM/eval_llm.json",
    #         "data/results/SEEDS/eval_seeds.json",
    #     )

    domains = ["JANUS", "SQL", "REDIS", "B", "MLIR", "CLOUDFORMATION", "CSV", "HTML"]
    domains = ["REDIS", "JANUS", "SQL", "B", "CSV", "HTML", "MLIR", "CLOUDFORMATION"]
    easy_domains = ["JANUS", "SQL", "REDIS", "B", "CSV", "JSON", "HTML"]
    hard_domains = ["MLIR", "CLOUDFORMATION"]
    # compare_grammar_complexity(
    #     domains,
    #     "data/results/grammars/results_grammars.json",
    # )
    # plot_seed_lengths(domains, "data/results/SEEDS/eval_seeds.json")
    # compare_circuit_size(easy_domains, "data/results/PC/eval_scalability.json")
    # compare_train_time(
    #     easy_domains,
    #     "data/results/PC/eval_PC_model.json",
    #     "data/results/SEEDS/eval_seeds.json",
    # )
    # compare_compilation_time(
    #     hard_domains,
    #     "data/results/PC/eval_PC_model.json",
    #     "data/results/SEEDS/eval_seeds.json",
    # )

    # domains = ["SQL", "JANUS", "REDIS", "B", "CSV", "HTML", "JSON"]
    # comparison_likelihood_domains_with_HMM(
    #     domains,
    #     "data/results/PC/eval_PC_model.json",
    #     "data/results/PCFG/eval_PCFG.json",
    #     "data/results/LLM/eval_llm.json",
    #     "data/results/PC-HMM/eval_PC_HMM.json",
    # )

    domains = ["SQL", "JANUS", "REDIS", "B", "CSV", "HTML", "JSON"]
    # comparison_perplexity_domains_with_HMM(
    #     domains,
    #      "data/results/PC/eval_PC_model_with_perplexity_bis.json",
    #     "data/results/PCFG/eval_PCFG_with_perplexity_bis.json",
    #     "data/results/LLM/eval_llm_with_perplexity_bis.json",
    #     "data/results/PC-HMM/eval_PC_HMM_with_perplexity_bis.json",
    # )

    

    df_filtered = comparison_perplexity_domains_with_HMM_only_realistic_data(domains,
         "data/results_october/PC/eval_PC_model.json",
        "data/results_october/PCFG/eval_PCFG.json",
        "data/results_october/LLM/eval_llm.json",
        "data/results/PC-HMM/eval_PC_HMM_with_perplexity_bis.json",
        "data/results/SEEDS/eval_seeds_updated.json")
    
    latex = df_filtered_to_latex_table(df_filtered,caption= "Perplexity per Domain", label="tab:perplexity_domain_comparison")
    print(latex)