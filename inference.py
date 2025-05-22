import torch
from cfg2pc.query import marginal_query, marginal_query_cond
from cfg2pc.SQL_prob import marginal_proba, conditional_proba



def query_marginals(model, lit_map, max_length, lit_size):
    toks = ["SELECT", "DOT", "ORDER", "BY", "FROM", "STAR"]

    for tok in toks:
        print(" --MARGINAL QUERY FROM PC --")
        prob = marginal_query(model, tok, lit_map, lit_size, max_length)
    
        print(f"P({tok})={prob:.4f}")
        print("--MARGINAL QUERY FROM SEEDS --")
        prob = marginal_proba(tok, "data/input/seeds/SQL", "data/input/grammars/SQL/SQLSimplifiedParser.g4")

        print(f"P({tok})={prob:.4f}")

        print()

def query_bi_conds(model, lit_map, max_length, lit_size):
    seqs = [["SELECT", "FROM"], ["ORDER", "BY"], ["BY", "ORDER"]]

    for seq in seqs:
        tok = seq[0]
        tok2 = seq[1]

        print(" --CONDITIONAL QUERY FROM PC --")
        prob = marginal_query_cond(model, tok, tok2, lit_map, lit_size, max_length)
    
        print(f"P({tok})={prob:.4f}")
        print("--CONDITIONAL QUERY FROM SEEDS --")
        prob = conditional_proba(tok, tok2, "data/input/seeds/SQL", "data/input/grammars/SQL/SQLSimplifiedParser.g4")

        print(f"P({tok})={prob:.4f}")

        print()



if __name__ == "__main__":
    model = torch.load("data/output/model/SQL/SQL-no-generate-35.pt", weights_only=False)
    model.eval()
    lit_map = model.lit_map
    max_length = 25 
    lit_size = max(l for l in lit_map.values()) + 1


    query_marginals(model, lit_map, max_length, lit_size)
    query_bi_conds(model, lit_map, max_length, lit_size)
