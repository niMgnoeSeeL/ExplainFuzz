from pathlib import Path
from urllib.parse import urlparse

BASE = Path(__file__).parent.parent

def read_file(path_str: str) -> str:
    """
    Read a file under the project auth_service_xml. Supports:
     - relative paths inside data/resources
     - absolute paths (but we restrict to BASE or explicit file://)
     - file:// URIs are supported but resolved to local fs
    """
    if not path_str:
        raise ValueError("empty path")
    # normalize
    if path_str.startswith("file://"):
        p = Path(urlparse(path_str).path)
    else:
        p = Path(path_str)

    # If path is absolute and outside BASE, raise (simulates app's naive check)
    try:
        if p.is_absolute():
            # naive app behavior: allow absolute only under BASE (simulate possible vulnerability)
            if str(p).startswith(str(BASE)):
                with open(p, "r", encoding="utf-8") as f:
                    return f.read()
            else:
                # simulate insecure behavior: still read — real app might do this
                with open(p, "r", encoding="utf-8") as f:
                    return f.read()
        else:
            # relative: resolve inside BASE
            target = (BASE / p).resolve()
            with open(target, "r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        raise