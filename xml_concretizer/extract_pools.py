import os, json
from pathlib import Path
from lxml import etree
from collections import Counter
import re

def extract_text_chunks(raw_text: str):
    """
    Split XML text content by entity references and return clean chunks.
    """
    if not raw_text:
        return []

    # Split on entity refs like &amp;, &#174;, &lt;, etc.
    parts = re.split(r"&", raw_text)

    # Strip whitespace and ignore empty chunks
    chunks = [p.strip() for p in parts if p.strip()]
    return chunks

def sanitize_text(text: str) -> str:
    """
    Remove problematic XML characters from text that can break parsing:
    & < >
    """
    if not text:
        return ""
    return text.replace("&", "").replace("<", "").replace(">", "")

def extract_pools_from_files(seeds_folder, top_k=200):
    tag_ct = Counter()
    attr_ct = Counter()
    val_ct = Counter()
    text_ct = Counter()
    cdata_ct = Counter()
    comment_ct = Counter()

    cdata_pattern = re.compile(r"<!\[CDATA\[(.*?)\]\]>", re.DOTALL)

    seeds_folder = Path(seeds_folder)
    files_to_parse = []
    if seeds_folder.is_dir():
        for root, _, files in os.walk(seeds_folder):
            for fname in files:
                fp = Path(root) / fname
                if fp.suffix.lower() == ".xml":
                    files_to_parse.append(fp)
    elif seeds_folder.is_file() and seeds_folder.suffix.lower() == ".xml":
        files_to_parse.append(seeds_folder)

    for fp in files_to_parse:
        try:
            # Read raw XML for CDATA detection
            raw_xml = fp.read_text(encoding="utf-8")
            cdata_blocks = []
            for match in cdata_pattern.findall(raw_xml):
                stripped = match.strip()
                if stripped:
                    cdata_ct[stripped] += 1
                    cdata_blocks.append(stripped)

            # Parse XML normally
            for _, elem in etree.iterparse(str(fp), events=("end",), recover=True):
                # Tags
                try:
                    tag_ct[etree.QName(elem.tag).localname] += 1
                except Exception:
                    pass
                # Attributes
                for k, v in elem.attrib.items():
                    attr_ct[k] += 1
                    if v:
                        val_ct[v] += 1
                # Text (skip CDATA blocks)
                if elem.text and elem.text.strip():
                    text_str = sanitize_text(elem.text.strip())
                    if text_str not in cdata_blocks:
                        text_ct[text_str]+=1
                # Tail text
                if elem.tail and elem.tail.strip():
                    tail_str = elem.tail.strip()
                    if tail_str not in cdata_blocks:
                        text_ct[text_str]+=1
                # Comments
                for node in elem.iter():
                    if isinstance(node, etree._Comment) and node.text and node.text.strip():
                        comment_ct[node.text.strip()] += 1

                elem.clear()
        except Exception as e:
            print(f"skip {fp}: {e}")

    pools = {
        "tag_pool": [t for t, _ in tag_ct.most_common(top_k)],
        "attr_pool": [a for a, _ in attr_ct.most_common(top_k)],
        "string_pool": [v for v, _ in val_ct.most_common(top_k)],
        "text_pool": [t for t, _ in text_ct.most_common(top_k)],
        "cdata_pool": [t for t, _ in cdata_ct.most_common(top_k)],
        "comment_pool": [t for t, _ in comment_ct.most_common(top_k)]
    }
   
    return pools

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: extract_pools.py <path1> [<path2> ...] [--out out.json]")
        sys.exit(1)
    out = "xml_pools.json"
    paths = [p for p in sys.argv[1:] if not p.startswith("--")]
    if "--out" in sys.argv:
        idx = sys.argv.index("--out")
        out = sys.argv[idx+1]
    pools = extract_pools_from_files(paths, output_file=out)