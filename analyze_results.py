import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import numpy as np
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
    domain, results_PC_file, results_PCFG_file, results_LLM_file, results_seeds_file
):
    df_PC = get_df_domain(domain, results_PC_file)
    df_PCFG = get_df_domain(domain, results_PCFG_file)
    df_LLM = get_df_domain(domain, results_LLM_file)
    df_seeds = get_df_domain(domain, results_seeds_file)
    df = pd.concat([df_PC, df_PCFG, df_LLM], ignore_index=True)

    # --- Plot 1: Log-Likelihood vs Max Length ---

    def adjust_lightness(color, factor):
        """Lighten or darken a color by multiplying (factor <1 = darker, >1 = lighter)."""
        r, g, b = to_rgb(color)
        return (min(r * factor, 1), min(g * factor, 1), min(b * factor, 1))

    # Define base colors for each method
    base_colors = {
        "PC": sns.color_palette("muted")[2],
        "PCFG": sns.color_palette("muted")[1],
        "LLM": sns.color_palette("muted")[0],
    }

    # Create custom palette for method + mode
    custom_palette = {}
    for method in base_colors:
        base = base_colors[method]
        custom_palette[f"{method} / with-generate"] = adjust_lightness(base, 1.3)
        custom_palette[f"{method} / no-generate"] = adjust_lightness(base, 0.8)

    # Create method/mode label
    df["method_mode"] = df["method"] + " / " + df.get("mode", "")
    df_filtered = df[df["mode"] == "no-generate"]

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
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df_filtered,
        x="max_length",
        y="avg-loglikelihood",
        hue="method",
        marker="o",
    )
    plt.title(f"Log-Likelihood vs Max Length ({domain})")
    plt.xlabel("Max Length")
    plt.ylabel("Average Log-Likelihood")
    plt.legend(title="Method / Mode")
    # plt.xticks([15])
    plt.tight_layout()
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
        data=df_filtered, x="domain", y="avg-loglikelihood", hue="method", errorbar="sd"
    )
    plt.title("Average Log-Likelihood (no-generate) Across Domains")
    plt.xlabel("Domain")
    plt.ylabel("Average Log-Likelihood")
    plt.tight_layout()
    plt.legend(title="Method")
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
    domain = "JSON"
    # analyze_results_PC(domain, "data/results/PC/eval_PC_model.json")
    # # analyze_results_PCFG(domain, "data/results/PCFG/eval_PCFG_fix_depth.json")

    # compare_results_model(
    #     domain,
    #     "data/results/PC/eval_PC_model.json",
    #     "data/results/PCFG/eval_PCFG.json",
    #     "data/results/LLM/eval_llm.json",
    #     "data/results/SEEDS/eval_seeds.json",
    # )
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
    compare_grammar_complexity(
        domains,
        "data/results/grammars/results_grammars.json",
    )
    # plot_seed_lengths(domains, "data/results/SEEDS/eval_seeds.json")
    # compare_circuit_size(easy_domains, "data/results/PC/eval_scalability.json")
    # compare_train_time(
    #     easy_domains,
    #     "data/results/PC/eval_PC_model.json",
    #     "data/results/SEEDS/eval_seeds.json",
    # )
    compare_compilation_time(
        hard_domains,
        "data/results/PC/eval_PC_model.json",
        "data/results/SEEDS/eval_seeds.json",
    )

    domains = ["SQL", "JANUS", "REDIS", "B", "CSV", "HTML", "JSON"]
    # comparison_likelihood_domains(
    #     domains,
    #     "data/results/PC/eval_PC_model.json",
    #     "data/results/PCFG/eval_PCFG.json",
    #     "data/results/LLM/eval_llm.json",
    # )
