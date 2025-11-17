from lxml import etree
from pathlib import Path

def load_config(path: Path):
    # Very simple loader: returns a dict of simple config values
    try:
        tree = etree.parse(str(path))
        root = tree.getroot()
        cfg = {}
        for child in root:
            cfg[child.tag] = child.text
            for k, v in child.items():
                cfg[f"{child.tag}.{k}"] = v
        return cfg
    except Exception:
        return {}