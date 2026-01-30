# ExplainFuzz

**ExplainFuzz** is a grammar-based fuzzing framework that generates explainable and structurally realistic test inputs by combining grammar refactoring, probabilistic circuit (PC) learning, and semantic concretization.

This repository contains the artifact for the paper submission.

---

## Overview

ExplainFuzz provides:

- **Grammar Refactoring**: Automatically converts ANTLR grammars to Chomsky Normal Form (CNF) for PC compilation.
- **Probabilistic Circuit Learning**: Builds tractable probabilistic models from grammars and learns input distributions from seed corpora.
- **Probabilistic Inference**: Supports marginal, conditional, and evidence queries over the learned distribution.
- **Semantic Concretization**: Transforms syntactically valid inputs into semantically meaningful ones (e.g., executable SQL queries).
- **Multi-Domain Support**: Tested on SQL, XML, JSON, HTML, CSV, REDIS, MLIR, and CloudFormation grammars.

---

## Requirements

- **OS**: Ubuntu 20.04+ (tested on Ubuntu 22.04)
- **Python**: 3.10+ (tested on 3.13)
- **Java**: JDK 11+ (for ANTLR)
- **PostgreSQL**: Development libraries (`libpq-dev`)

---

## Project Structure

```
ExplainFuzz/
├── app.py                    # Main UI application
├── main.py                   # Core pipeline orchestration
├── inference.py              # Probabilistic query interface
├── domains_config.json       # Domain configurations
├── bug_specs.py              # Bug specifications for evaluation
├── GrammarRefactoring/       # ANTLR grammar → CNF conversion
├── cfg2pc/                   # Probabilistic circuit compilation & training
├── grammarinator_fuzzing/    # Input generation module
├── custom_generator_sql/     # SQL semantic concretization
├── data/                     # Grammars, seeds, and results
│   ├── grammars/             # ANTLR grammar files
│   ├── seeds/                # Seed corpora per domain
│   └── results/              # Evaluation results
└── eval_*.py                 # Evaluation scripts
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ExplainFuzz
git submodule update --init --recursive
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install System Dependencies

```bash
sudo apt-get update
sudo apt-get install -y libpq-dev openjdk-11-jdk
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('words')"
```

### 5. Install ANTLR

```bash
wget https://www.antlr.org/download/antlr-4.13.0-complete.jar
echo "ANTLR_JAR_PATH=$(pwd)/antlr-4.13.0-complete.jar" > GrammarRefactoring/.env
```

### 6. Configure API Key (Optional)

For SQL semantic concretization, set up a Google AI API key:

```bash
echo "API_KEY=your-api-key" > .env
```

Get an API key from: https://makersuite.google.com/app/apikey

### 7. Install Project Modules

```bash
pip install -e GrammarRefactoring/
pip install -e grammarinator_fuzzing/
pip install -e cfg2pc/
pip install -e custom_generator_sql/
```

---

## Quick Start

### Launch the UI

```bash
python app.py
```

The Gradio interface allows you to:
- Select a domain (SQL, XML, JSON, etc.)
- Generate inputs from the learned distribution
- Run probabilistic inference queries

### Command-Line Usage

Build and train a model for a specific domain:

```python
from main import build_model

model = build_model(domain="SQL")
```

Generate inputs:

```python
samples = model.sample(n=100)
```

---

## Reproducing Evaluation Results

### Scalability and Perplexity Evaluation

```bash
python eval_scalability_perplexity.py
```

### Inference Query Evaluation

```bash
python eval_inference.py
```

### Bug-Finding Evaluation

```bash
python eval_multi_bug.py
```

### Visualizing Results

Open and run the Jupyter notebook:

```bash
jupyter notebook visualize_results_all_evaluations_issta.ipynb
```

Results are saved to `data/results/` and figures to `data/results/figures/`.

---

## Supported Domains

| Domain | Grammar | Semantic Concretization |
|--------|---------|------------------------|
| SQL    | SQLSimplified.g4 | Yes (LLM-based) |
| XML    | XMLParser.g4 | No |
| JSON   | JSON.g4 | No |
| HTML   | HTMLParser.g4 | No |
| CSV    | CSV.g4 | No |
| REDIS  | redis.g4 | No |
| MLIR   | MLIR.g4 | No |
| CloudFormation | JSON.g4 | No |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `psycopg2-binary` build fails | Install `libpq-dev`: `sudo apt-get install libpq-dev` |
| NLTK `words` not found | Run: `python -c "import nltk; nltk.download('words')"` |
| Module not found errors | Reinstall project modules with `pip install -e` |
| Google AI API key error | Create `.env` file with `API_KEY=your-key` |

---

## License

This project is released for academic research purposes.
