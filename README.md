# ExplainFuzz

**ExplainFuzz** generates explainable and structurally realistic test inputs by combining grammar refactoring, probabilistic circuit learning, and optional semantic concretization.

---

## 🔍 Overview

ExplainFuzz automatically:
- Refactors ANTLR grammars to a CNF form.
- Builds a Probabilistic Circuit (PC) from the grammar.
- Learns input distributions from a corpus using PC weight optimization.
- Generates realistic inputs that conform to the learned grammar (for the SQL domain).

This allows fuzzing tools to produce inputs that better reflect real-world structures, improving testing efficiency and semantic coverage.

---

## 🛠 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ExplainFuzz.git
cd ExplainFuzz
```

In order to clone the repo with the submodules, you can run : 

```
git submodule update --init --recursive
```


To pull from existing submodules : 
````
git pull --recurse-submodules 
````


### 2. Install dependencies

It is recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```
Install Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Install ANTLR(v4.13.0)

Download the ANTLR tool:

```bash
wget https://www.antlr.org/download/antlr-4.13.0-complete.jar
```

Create an `.env` file in the root of the submodule `GrammarRefactoring` and add the path to this jar `ANTLR_JAR_PATH=`


### 4. Install project modules
```bash
pip install -e GrammarRefactoring/
pip install -e grammarinator_fuzzing/
pip install -e custom_generator_sql/
pip install -e cfg2pc/
```


## 🚀 Usage

The user interface is defined in `app.py`. To launch it, run:
```
python app.py
```

From the UI, you can select a specific domain and either generate new inputs or experiment with the inference query functionality.

