from pathlib import Path
from typing import Set, Union

ROOT_PROJECT = Path("xml_concretizer/auth_service_xml").resolve()

def gen_sensitive_paths(root: Union[str, Path] = ROOT_PROJECT):
    root_path = Path(root)
    if not root_path.exists() or not root_path.is_dir():
        raise ValueError(f"root must be an existing directory: {root}")
    
    resources = root_path / "data" / "resources"

    filenames = [
        "secrets.txt", "app.log", "cookies.json", "db_config.yml",
        "server.key", "session_tokens.txt", ".env", "api_key.txt",
    ]

    project_local = set()
    for name in filenames:
        f = resources / name
        if f.exists():
            project_local.add(str(Path("data/resources") / f.name))  # relative variant

    # System-sensitive attacker targets
    system = gen_system_sensitive_paths()
    return {"project_local": project_local, "system": system}

def gen_all_paths_project(root: Union[str, Path] = ROOT_PROJECT) -> Set[str]:
    """
    Walk `root` recursively and return a set of relative file paths (strings).
    Each returned path is the path *relative to root*, e.g. "data/resources/secrets.txt".

    - Only regular files are returned (no directories).
    - Uses POSIX-style separators (forward slashes) for portability.
    - If `root` does not exist or is not a directory, raises ValueError.
    """
    root_path = Path(root)
    if not root_path.exists() or not root_path.is_dir():
        raise ValueError(f"root must be an existing directory: {root}")

    rel_paths: Set[str] = set()
    for p in root_path.rglob("*"):
        if p.is_file():
            try:
                rel = p.relative_to(root_path).as_posix()
            except Exception:
                # fallback to os.path.relpath if relative_to fails for any reason
                rel = Path(p).resolve().relative_to(root_path.resolve()).as_posix()
            rel_paths.add(rel)
    return rel_paths

def gen_system_sensitive_paths():
    # System-sensitive attacker targets
    system = {
        "/etc/passwd", "/etc/hosts", "/etc/hostname",
    }
    system |= {"file://" + p for p in list(system)}
    return system

def gen_all_context_paths():
    project_local = gen_all_paths_project()
    system = gen_system_sensitive_paths()
    return {"project_local": project_local, "system": system}

