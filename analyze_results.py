import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb


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


def compare_results_model(domain, results_PC_file, results_PCFG_file, results_LLM_file):
    df_PC = get_df_domain(domain, results_PC_file)
    df_PCFG = get_df_domain(domain, results_PCFG_file)
    df_LLM = get_df_domain(domain, results_LLM_file)
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
        data=df,
        x="max_length",
        y="avg-loglikelihood",
        hue="method",
        style="mode",
        marker="o",
    )
    plt.title(f"Log-Likelihood vs Max Length ({domain})")
    plt.xlabel("Max Length")
    plt.ylabel("Average Log-Likelihood")
    plt.legend(title="Method / Mode")
    plt.tight_layout()
    plt.show()

    # --- Plot 2: Log-Likelihood vs Query Type (mode) ---
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x="mode", y="avg-loglikelihood", hue="method", errorbar="sd")
    plt.title(f"Log-Likelihood vs Query Type ({domain})")
    plt.xlabel("Query Type")
    plt.ylabel("Average Log-Likelihood")
    plt.tight_layout()
    plt.show()


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


if __name__ == "__main__":
    # domain = "JANUS"
    # analyze_results_PC(domain, "data/results/PC/eval_PC_model.json")
    # # analyze_results_PCFG(domain, "data/results/PCFG/eval_PCFG_fix_depth.json")

    # compare_results_model(
    #     domain,
    #     "data/results/PC/eval_PC_model.json",
    #     "data/results/PCFG/eval_PCFG.json",
    #     "data/results/LLM/eval_llm.json",
    # )

    domains = ["SQL", "JANUS", "REDIS", "B"]
    comparison_likelihood_domains(
        domains,
        "data/results/PC/eval_PC_model.json",
        "data/results/PCFG/eval_PCFG.json",
        "data/results/LLM/eval_llm.json",
    )
