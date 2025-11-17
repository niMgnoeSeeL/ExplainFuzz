"""
Run this script with a single argument: the path to an XML file (a "request").
It will parse the XML and perform a few operations:
 - run an XPath query against data/users.xml if a 'query' element/attribute exists
 - read filesystem paths if a 'path' attribute is present (via storage.read_file)
 - do integer parsing for numeric fields (possible overflow)
It logs file accesses in ./app/runtime.log for the harness to inspect.
"""
import sys
import json
import logging
from lxml import etree
from pathlib import Path
import re

from . import storage, config_loader

logging.basicConfig(filename=str(Path(__file__).parent / "runtime.log"),
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

NUMERIC_XSD_TYPES = {"xs:int", "xs:integer", "xs:float", "xs:double"}

def process_request(path_to_xml, allow_external_entities=False):
    # Load config (simple)
    cfg = config_loader.load_config(Path(__file__).parent.parent / "config" / "service_config.xml")
    # parser: by default we do NOT resolve external entities unless explicitly allowed
    parser = etree.XMLParser(resolve_entities=allow_external_entities, recover=True)
    try:
        tree = etree.parse(str(path_to_xml), parser)
        root = tree.getroot()
    except Exception as e:
        print(json.dumps({"ok": False, "error": f"parse_error: {e}"}))
        return 2
    if root is None:
        print(json.dumps({
            "ok": False,
            "error": f"empty_or_invalid_root: could not parse"
        }))
        return 2
    
    # 1) If request contains a <query select="..."> attribute OR text content, run XPath on data/users.xml
    
    for q in root.xpath("//query"):
        sel = q.get("select") or (q.text.strip() if q.text else None)
        if sel:
            try:
                users_tree = etree.parse(str(Path(__file__).parent.parent / "data" / "users.xml"))
                res = users_tree.xpath(sel)
                logging.info(f"XPath executed; selector={sel}; matches={len(res)}")
            except Exception as e:
                logging.exception(f"XPath error for selector={sel}: {e}")

    # 2) If any element has attribute 'path' or 'file', attempt to read it via storage
    for elem in root.iter():
        for a_name in elem.keys():
            if any(k in a_name.lower() for k in ("path", "file", "src", "href")):
                val = elem.get(a_name)
                try:
                    content = storage.read_file(val)
                    logging.info(f"read_file path={val} len={len(content)}")
                except Exception as e:
                    logging.exception(f"read_file failed path={val}: {e}")

    # 3) Parse numeric-like attributes (simulate arithmetic)
    numeric_names = ["amount","repeat","limit","price"]
    for elem in root.iter():
        for a_name, a_val in elem.items():
            if a_val and a_name in numeric_names:
                try:
                    v = float(a_val)
                except Exception as e:
                    logging.exception(f"numeric parse error {a_name}={a_val}: {e}")

    print(json.dumps({"ok": True, "message": "processed"})) 
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: process_request.py <request.xml> [--allow-xxe]")
        sys.exit(1)
    allow_xxe = "--allow-xxe" in sys.argv
    rc = process_request(sys.argv[1], allow_external_entities=allow_xxe)
    sys.exit(rc)