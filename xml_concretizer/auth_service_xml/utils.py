ENTITIES = {
    # --- people ---
    "a": "alice",
    "b": "bob",

    # --- files & paths ---
    "f": "/home/alice/report.txt",
    "g": "/tmp/cache.bin",
    # --- actions / requests ---
    "k": "upload",
    "l": "download",

    # --- message / content snippets ---
    "q": "Access denied",
    "r": "Operation completed successfully",
    # --- numeric or misc values ---
    "w": "true",
    "x": "false"
}

def wrap_with_doctype(xml_string: str) -> str:
    """
    Wrap the XML with an internal DTD defining the allowed entities.
    Automatically infers the root tag name.
    """
    import re

    # Extract root tag name (first opening tag)
    match = re.match(r"\s*<([a-zA-Z0-9_\-:]+)", xml_string)
    root_name = match.group(1) if match else "root"

    # Construct internal DTD
    entity_text ="\n".join([f'<!ENTITY {key} "{val}">' for key,val in ENTITIES.items()])
    doctype = f'<!DOCTYPE {root_name} [\n{entity_text}\n]>'

    # Wrap it all together
    return f'<?xml version="1.0"?>\n{doctype}\n{xml_string}'
