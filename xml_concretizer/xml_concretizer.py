# xml_concretizer.py
import os
import random
import string
import json 
from typing import List, Dict, Any, Tuple, Optional
from lxml import etree
import typing
import re


from xml_concretizer.auth_service_xml.utils import ENTITIES
from xml_concretizer.extract_pools import extract_pools_from_files
from xml_concretizer.xsd_to_metadata import get_main_tags, get_metadata

# ----------------------
# Default pools
# ----------------------
DEFAULT_TAG_NAMES = [
    "config", "book", "title", "author", "item", "entry", "product", "element",
    "data", "article", "section", "note", "library", "catalog", "image"
]
DEFAULT_ATTR_NAMES = ["id", "name", "src", "href", "path", "key", "value", "genre", "type", "option"]
DEFAULT_STRING_VALUES = ["value", "true", "false", "Alice", "Bob", "1", "setting1"]
DEFAULT_CDATA = [
            "Example CDATA content",
            "Raw <xml> inside CDATA", 
            "",
            "simple text",
            "note: no markup here",
        ]
DEFAULT_COMMENTS = ["generated", "placeholder", ""]
DEFAULT_TEXT = ["text", "content", "sample"]
GENERIC_IDENTIFIERS = ["user", "record", "account", "item", "entry", "name", "username", "id"]
GENERIC_VALUES = ["alice", "bob", "admin", "guest", "100", "0", "error"]

# ----------------------
# Context object
# ----------------------
class ConcretizerContext:
    def __init__(
        self,
        corpus_paths: Optional[List[str]] = None,
        xsd_path: Optional[str] = None,
        seed_keywords: Optional[List[str]] = None,
        all_paths: Optional[List[str]] = None,
        mode: str = "mixed",       # "realistic" | "mixed" | "aggressive"
        mix_ratio: float = 0.8,
        seed: Optional[int] = None,
        schema_folder:Optional[str]=None
    ):
        self.corpus_paths = corpus_paths or []
        self.xsd_path = xsd_path
        self.seed_keywords = seed_keywords or []
        self.all_paths = all_paths or [] # sensitive path
        self.mode = mode
        self.mix_ratio = mix_ratio
        self.seed = seed
        self.schema_metadata = get_metadata(schema_folder, file_save_metadata="xml_concretizer/metadata.json")
        self.main_tags = get_main_tags(self.schema_metadata) if self.schema_metadata else {}
        self.entities = ENTITIES

# ----------------------
# Helpers
# ----------------------
def choose(pool: List[str], rng: random.Random) -> str:
    if not pool:
        return ""
    return rng.choice(pool)

def sanitize_attr_value(val: str) -> str:
    """Ensure value is XML-escaped and quoted (without quotes; caller adds them)."""
    return val.replace("&", "&amp;").replace('"', "&quot;")

def edge_sampler(slot_type: str, rng: random.Random) -> str:
    """Generate edge-case/rare values for fuzzing."""
    if slot_type == "Name":
        return rng.choice(["", "!!@@##", "A"*128, "§§§§", "ΔΩπ"])
    elif slot_type == "STRING":
        choice = rng.randint(0,4)
        if choice == 0:
            return "../" + "".join(rng.choices(string.ascii_letters, k=10))
        elif choice == 1:
            return "/etc/passwd"
        elif choice == 2:
            return "A"*rng.randint(100,5000)
        elif choice == 3:
            return "".join(rng.choices(string.printable, k=50))
        else:
            return ""
    elif slot_type == "ID":
        return "id_" + "".join(rng.choices(string.ascii_letters+string.digits, k=8))
    return "EDGE"

def random_path_or_url(rng: random.Random) -> str:
    """
    Generate a random filesystem path or URL using the provided random generator.
    Returns either a path (e.g., "dir1/dir2/file.txt") or a URL (e.g., "http://example.com/file.txt").
    """
    def random_name(length=6):
        return ''.join(rng.choices(string.ascii_lowercase + string.digits, k=length))

    # Randomly decide whether to generate URL or path
    is_url = rng.random() < 0.5

    # Random depth of directories
    depth = rng.randint(1, 3)
    dirs = [random_name(rng.randint(3, 8)) for _ in range(depth)]
    
    # Random file name
    file_name = random_name(rng.randint(4, 10))
    # Random extension
    extension = rng.choice(["txt", "pdf", "xml", "json"])
    file_name += f".{extension}"

    path = "/".join(dirs + [file_name])

    if is_url:
        domain = random_name(rng.randint(5, 10)) + ".example.com"
        return f"http://{domain}/{path}"
    else:
        return path

# -------------------------
# Numeric fuzzing helpers (no hidden probabilities)
# -------------------------

def sanitize_attr_value(val: str) -> str:
    """Escape quote characters and collapse problematic whitespace."""
    if val is None:
        return ""
    val = str(val)
    val = val.replace('"', "'")
    val = re.sub(r'\s+', ' ', val)
    return val

_INT32_MAX = 2**31 - 1
_INT32_MIN = -2**31
_INT64_MAX = 2**63 - 1
_INT64_MIN = -2**63

def _mutate_decimal_string(seed: str, rng: random.Random) -> str:
    """Apply small random edits to a numeric seed string to simulate plausible corruption."""
    s = seed
    ops = [
        "insert_digit", "delete_digit", "shuffle", "repeat", "append_chars", "prefix_sign"
    ]
    op = rng.choice(ops)

    if op == "insert_digit":
        idx = rng.randint(0, len(s))
        d = str(rng.randint(0,9))
        s = s[:idx] + d + s[idx:]
    elif op == "delete_digit" and len(s) > 1:
        idx = rng.randint(0, len(s)-1)
        s = s[:idx] + s[idx+1:]
    elif op == "shuffle":
        chars = list(s)
        rng.shuffle(chars)
        s = "".join(chars)
    elif op == "repeat":
        times = rng.randint(2,4)
        s = s * times
    elif op == "append_chars":
        s += rng.choice(["abc", "xx", ".0.1", "eX", "NaN"])
    elif op == "prefix_sign":
        s = ("-" if rng.random() < 0.5 else "+") + s
    return s

def gen_numeric_fuzz_for_type(attr_type: str, rng: random.Random, string_pool: List[str]) -> str:
    """
    Choose a mutation operator uniformly and produce a numeric-like or malformed string.
    Operators: normal, boundary, overflow, malformed, scientific, mutate_seed.
    """
    operators = ["normal", "overflow"]
    op = rng.choices(
        operators,
        weights=[0.97,0.02], k=1
    )[0]

    # NORMAL: reasonable value
    if op == "normal":
        if attr_type in ("xs:int", "xs:integer"):
            # xs:int is signed 32-bit
            return str(rng.randint(0, 2**32 - 1))
        if attr_type == "xs:long":
            # xs:long is signed 64-bit
            return str(rng.randint(0, 2**63 - 1))
        if attr_type in ("xs:float",):
            # float32: approx ±3.4028235e+38
            val = rng.uniform(-3.4e38, 3.4e38)
            return f"{val:.6g}"
        if attr_type == "xs:double":
            # float64: approx ±1.7976931348623157e+308
            val = rng.uniform(-1.7e308, 1.7e308)
            return f"{val:.12g}"

    # OVERFLOW: clearly exceed plausible fixed-width ranges
    if op == "overflow":
        if attr_type in ("xs:int", "xs:integer"):
            # overflow just beyond 32-bit range
            return str(rng.randint(_INT32_MAX + 1, _INT32_MAX * 2))
        if attr_type == "xs:long":
            # overflow just beyond 64-bit range, not astronomically large
            return str(rng.randint(_INT64_MAX + 1, _INT64_MAX * 2))
        if attr_type == "xs:float":
            # produce large exponent that a float32 cannot represent
            return f"1e{rng.randint(40, 100)}"
        if attr_type == "xs:double":
            return f"1e{rng.randint(309, 1000)}"
        return str(rng.randint(_INT32_MAX + 1, _INT64_MAX))


    # fallback
    return "0"

# ----------------------
# Helper functions for CDATA content
# ----------------------

# generators for "risky" CDATA content categories
def gen_embedded_markup():
    # small HTML/XML fragment
    tags = ["div","span","script","b","i","user","policy"]
    tag = random.choice(tags)
    inner = random.choice(["admin","<username>alice</username>", "1 OR 1=1", ""])
    # sometimes include attributes
    if random.random() < 0.4:
        return f"<{tag} class='x'>{inner}</{tag}>"
    return f"<{tag}>{inner}</{tag}>"

def gen_script_like():
    funcs = ["alert", "fetch", "eval", "console.log"]
    fn = random.choice(funcs)
    arg = random.choice(["'xss'","'/data'","token"])
    return f"{fn}({arg});"

def gen_sql_like():
    items = ["SELECT * FROM users WHERE username='admin';",
             "DROP TABLE sessions;",
             "INSERT INTO logs VALUES('x');"]
    return random.choice(items)

def gen_xpath_like(metadata):
    # use metadata keys to make realistic XPath expressions
    # pick an entity and a string field
    entity = random.choice(list(metadata.keys()))
    fields = [k for k,v in metadata[entity]["attributes"].items() if 'string' in v]
    field = random.choice(fields) if fields else "text"
    # small variety of selectors
    return random.choice([f"//{entity}/{field}", f"//{entity}[{field}='admin']"])

def gen_attr_fragment(metadata):
    # create attribute-like fragments: role="admin" or quota="100"
    entity = random.choice(list(metadata.keys()))
    attr, t = random.choice(list(metadata[entity]["attributes"].items()))
    val = random_value_for_type(t)
    return f'{attr}="{val}"'

def gen_file_fragment():
    paths = ["/etc/passwd","/var/log/app.log","C:\\Windows\\system.ini","/tmp/data.txt"]
    return random.choice(paths)


def generate_cdata_content(context, rng:random.Random,fallback_pool,high_signal_prob=0.18):
    """
    Return the inner string for a CDATA block (without the <![CDATA[ ]]> wrapper).
    high_signal_prob: probability to produce a "risky" CDATA block.
    """
    metadata = getattr(context, "schema_metadata", {})
    if rng.random() < high_signal_prob:
        try:
            # pick a risky category
            choice = rng.random()
            if choice < 0.2:
                return gen_embedded_markup()
            elif choice < 0.4:
                return gen_script_like()
            elif choice < 0.6:
                return gen_sql_like()
            elif choice < 0.8:
                return gen_xpath_like(metadata)
            else:
                # attribute or file fragments are lower-impact but plausible
                return rng.choice([gen_attr_fragment(metadata), gen_file_fragment()])
        except:
            return rng.choice(fallback_pool)
    else:
        return rng.choice(fallback_pool)

# ----------------------
# Helper functions to pick tag, value, attr
# ----------------------

def pick_main_tag(tag_pool: List[str], context, rng: random.Random) -> str:
    main_tags = getattr(context, "main_tags", {})
    if main_tags:
        return rng.choice(list(main_tags.keys())) 
    return rng.choice(tag_pool)

def pick_tag(tag_pool: List[str], context, rng: random.Random, prev_tag:str | None = None) -> str:
    metadata = getattr(context, "schema_metadata", {})
    if metadata:
        if prev_tag:
            subelements = metadata.get(prev_tag,{}).get("subelements",[])
            if subelements:
                return rng.choice(subelements)
            else:
                return rng.choice(list(metadata.keys()))
        else:
            return pick_main_tag(tag_pool,context,rng)
    return rng.choice(tag_pool)

def pick_attr_for_tag(
    tag_name: str,
    context,
    rng: random.Random,
    fallback_pool: Optional[List[str]] = None,
    forbidden: Optional[set] = None,
) -> str:
    metadata = getattr(context, "schema_metadata", {})
    fallback_pool = fallback_pool or []
    forbidden = forbidden or set()
    
    # 20% chance to produce a namespace confusion candidate
    if rng.random() < 0.20:
        prefix = chr(ord('a') + rng.randint(0, 25))
        candidate = f"xmlns:{prefix}"
        if candidate not in forbidden:
            return candidate

    # Try schema-driven attributes
    if metadata and tag_name in metadata and metadata[tag_name]["attributes"]:
        candidates = [k for k in metadata[tag_name]["attributes"].keys() if k not in forbidden]
        if candidates:
            return rng.choice(candidates)

    prefix = chr(ord('a') + rng.randint(0, 25))
    candidate = f"xmlns:{prefix}"
    if candidate not in forbidden:
        return candidate
    
    # Fallback to attribute pool
    # if fallback_pool:
    #     candidates = [a for a in fallback_pool if a not in forbidden]
    #     if candidates:
    #         return rng.choice(candidates)

    # If all options exhausted, make up a unique name
    base = "attr"
    i = 0
    while f"{base}_{i}" in forbidden:
        i += 1
    return f"{base}_{i}"

def generate_attr_value(tag_name: str, attr_name: str, string_pool: List[str], context, rng: random.Random) -> str:
    metadata = getattr(context, "schema_metadata", {})
    attr_type = metadata.get(tag_name, {}).get("attributes",{}).get(attr_name, "xs:string")
    all_paths = getattr(context, "all_paths", [])
    
    # Prioritize sensitive / special attributes
    if (attr_name in ("path", "file","src", "href") or attr_type == "xs:anyURI") and all_paths and rng.random() < getattr(context, "mix_ratio", 0.5):
        val = rng.choice(all_paths)
    elif attr_name.lower() in ("xpath","select", "query") and rng.random() < 0.3:
        val = gen_generic_xpath(rng=rng, string_pool=string_pool, aggression=0.3)
    # Type-driven generation
    elif attr_type in ("xs:int", "xs:integer","xs:double","xs:float","xs:long"):
        val = gen_numeric_fuzz_for_type(attr_type, rng, string_pool)
    elif attr_type == "xs:anyURI" or "xmlns" in attr_name:
        val = random_path_or_url(rng)
    else:
        val = rng.choice(string_pool)
    return sanitize_attr_value(val)



def generate_text_for_tag(current_tag, current_attribute, context, rng, text_pool):
    # --- Case 1: Attribute value generation ---

    if current_tag and current_attribute:
        return generate_attr_value(current_tag, current_attribute, text_pool, context, rng)

    # --- Case 2: Regular TEXT content generation ---
    # Normal valid text = random word, sometimes from pool
    p_from_pool = 0.7
    p_malformed = 0.1

    if rng.random() < p_from_pool and text_pool:
        text = rng.choice(text_pool)
    else:
        # Generate new random text
        length = rng.randint(3, 12)
        text = ''.join(rng.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_ ") for _ in range(length)).strip()   
    return text

def generate_random_name(rng:random.Random,min_length=3, max_length=10):
    """
    Generates a random but VALID name string according to the ANTLR grammar rules:
    Name: NameStartChar NameChar*

    Grammar definitions:
    - NameStartChar: [_:a-zA-Z] (must be the first character)
    - NameChar: NameStartChar | '-' | '.' | DIGIT (can be subsequent characters)

    Args:
        min_length (int): The minimum length of the generated name. Must be >= 1.
        max_length (int): The maximum length of the generated name.

    Returns:
        str: A randomly generated name string that conforms to the grammar.
    """
    # 1. Define character sets based on the grammar
    
    # NameStartChar: [_:a-zA-Z]
    name_start_chars = string.ascii_letters + '_:'
    
    # NameChar: NameStartChar | '-' | '.' | DIGIT 
    name_chars = name_start_chars + '-.' + string.digits
    
    # Ensure min_length is at least 1, as NameStartChar is mandatory
    if min_length < 1:
        min_length = 1
        
    # 2. Determine a random length
    length = rng.randint(min_length, max_length)
    
    # 3. Select the mandatory first character (NameStartChar)
    if not name_start_chars:
        return "" # Should not happen based on definition
        
    first_char = rng.choice(name_start_chars)
    
    # 4. Generate the remaining characters (NameChar)
    remaining_length = length - 1
    
    if remaining_length > 0:
        # random.choices is used for efficient selection of multiple characters
        remaining_chars = rng.choices(name_chars, k=remaining_length)
        
        # 5. Combine and return
        return first_char + "".join(remaining_chars)
    else:
        # Length was 1
        return first_char


def generate_entity_ref_val(context,rng:random.Random):
    text = rng.choice(list(context.entities.keys()) + ["lt", "gt", "amp", "apos", "quot"])
    return text

# Allowed XML 1.0 ranges (inclusive)
XML_ALLOWED_RANGES = [
    (0x9, 0x9),            # tab
    (0xA, 0xA),            # newline
    (0xD, 0xD),            # carriage return
    (0x20, 0xD7FF),
    (0xE000, 0xFFFD),
    (0x10000, 0x10FFFF),
]

def _range_size(r: Tuple[int,int]) -> int:
    return r[1] - r[0] + 1

# Precompute total size for weighted selection
_XML_TOTAL = sum(_range_size(r) for r in XML_ALLOWED_RANGES)

def _pick_random_allowed_cp(rng: random.Random, prefer_printable: bool) -> int:
    """
    Pick a random codepoint from XML allowed ranges.
    If prefer_printable is True, bias towards printable ASCII and basic BMP.
    """
    if prefer_printable and rng.random() < 0.75:
        # 75% of the time pick from printable ASCII (0x20..0x7E) which is inside allowed range
        return rng.randint(0x20, 0x7E)

    # Weighted pick across allowed ranges proportional to size
    pick = rng.randint(1, _XML_TOTAL)
    cum = 0
    for (start, end) in XML_ALLOWED_RANGES:
        size = _range_size((start, end))
        if pick <= cum + size:
            offset = pick - cum - 1
            return start + offset
        cum += size

    # Fallback (shouldn't happen)
    return 0x20

def generate_char_ref_text(rng: random.Random, prefer_printable: bool = True, hex_prob: float = 0.5) -> str:
    """
    Generate a valid XML 1.0 numeric character reference using rng.
    - prefer_printable: bias toward ASCII-printable characters for realism.
    - hex_prob: probability to output the hex form (&#x...;) rather than decimal.
    Returns a string like '&#65;' or '&#x41;'.
    """
    cp = _pick_random_allowed_cp(rng, prefer_printable)

    # Avoid returning CR/LF/TAB as the only output unless explicitly desired:
    if cp in (0x9, 0xA, 0xD):
        # occasionally allow, but usually pick a printable char instead
        if rng.random() > 0.10:  # 90% chance to replace with a printable char
            cp = rng.randint(0x20, 0x7E)

    if rng.random() < hex_prob:
        return f"&#x{cp:X};"
    else:
        return f"&#{cp};"

def _lit(s: str) -> str:
    """Return a safe single-quoted XPath literal (uses concat if necessary)."""
    if "'" not in s:
        return f"'{s}'"
    parts = s.split("'")
    pieces = []
    for i, p in enumerate(parts):
        if p:
            pieces.append(f"'{p}'")
        if i != len(parts) - 1:
            pieces.append('"\'"')
    return "concat(" + ", ".join(pieces) + ")"

def gen_generic_xpath(rng: random.Random | None = None,
                      string_pool: typing.Optional[typing.List[str]] = None,
                      aggression: float = 0.3,
                      max_steps: int = 3) -> str:
    """
    Generate a generic, project-agnostic XPath-like expression.
    - rng: random.Random instance (or None -> creates new one)
    - string_pool: optional small pool to use only for literal fragments (not full expressions)
    - aggression: probability to insert obvious injection constructs (tautologies, ORs)
    - max_steps: number of steps in path (controls complexity)
    """
    rng = rng or random.Random()
    pool_vals = [p for p in (string_pool or []) if isinstance(p, str) and len(p) < 30]
    ids = GENERIC_IDENTIFIERS
    vals = GENERIC_VALUES + pool_vals

    # pick a base step/name
    name = rng.choice(ids)
    prefix = rng.choice(["//", "/"]) if rng.random() < 0.7 else ""  # favor double-slash but not always

    # decide expression type
    types = ["step_only", "predicate_eq", "contains", "or_taut", "function", "union", "absolute"]
    weights = [0.2, 0.25, 0.15, 0.15, 0.1, 0.1, 0.05]
    style = rng.choices(types, weights=weights, k=1)[0]

    # helper to pick literal
    val = rng.choice(vals) if vals else rng.choice(GENERIC_VALUES)
    lit = _lit(str(val))

    if style == "step_only":
        # e.g. //user or /record
        steps = rng.randint(1, max_steps)
        return prefix + "/".join(rng.choice(ids) for _ in range(steps))

    if style == "predicate_eq":
        # //user[username='alice']
        idx_name = rng.choice(ids)
        return f"{prefix}{name}[{idx_name}={lit}]"

    if style == "contains":
        # contains(username, 'ali')
        part = (val[:max(1, len(val)//2)]) if isinstance(val, str) else val
        return f"{prefix}{name}[contains({rng.choice(['username','name','id'])}, {_lit(str(part))})]"

    if style == "or_taut":
        # username='alice' or '1'='1'
        if rng.random() < aggression:
            taut = rng.choice(["'1'='1'", "1=1"])
        else:
            taut = f"{rng.choice(ids)}={_lit(random.choice(vals))}"
        return f"{prefix}{name}[{rng.choice(ids)}={lit} or {taut}]"

    if style == "function":
        # starts-with or concat
        if rng.random() < 0.5:
            return f"{prefix}{name}[starts-with({rng.choice(['username','name'])}, {_lit(val[:3])})]"
        return f"{prefix}{name}[contains({rng.choice(['username','name'])}, {_lit(val[:3])})]"

    if style == "union":
        # //user[...] | //admin
        other = f"//{rng.choice(ids)}"
        return f"{prefix}{name}[{rng.choice(ids)}={lit}] | {other}"

    if style == "absolute":
        # absolute-looking path; generic (not sensitive-file specific)
        return f"/{rng.choice(ids)}/{rng.choice(ids)}[{rng.choice(ids)}={lit}]"

    # fallback
    return f"{prefix}{name}[{rng.choice(ids)}={lit}]"

def random_value_for_type(type_str:str,rng:random.Random,fallback_pool:List[str]):
    if type_str in ("xs:int", "xs:integer","xs:double","xs:float"):
        val = gen_numeric_fuzz_for_type(type_str, rng, fallback_pool)
    elif type_str in ("xs:anyURI"):
        val= random_path_or_url(rng)
    else:
        val = rng.choice(fallback_pool)
    return sanitize_attr_value(val)

def generate_random_comment(context, rng,fallback_pool,high_signal_prob=0.3):
    """
    Generate a COMMENT token content.
    high_signal_prob: probability to generate a comment that could trigger BUG09_comment_logic_bypass
    """
    metadata = getattr(context, "schema_metadata", {})
    if metadata and random.random() < high_signal_prob:
        # generate schema-based comment
        try:
            entity = random.choice(list(metadata.keys()))
            attr, type_ = random.choice(list(metadata[entity]["attributes"].items()))
            val = random_value_for_type(type_,rng,fallback_pool)
            comment_content = rng.choice([f'<{entity} {attr}="{val}"/>',f'{attr}="{val}'])
        except:
            comment_content = random.choice(fallback_pool)
    else:
        # generic comment
        comment_content = random.choice(fallback_pool)
    return comment_content

# ----------------------
# Main concretizer
# ----------------------
def concretize_token_list(
    tokens: List[str],
    *,
    context,
    rng: random.Random,
    tag_pool: Optional[List[str]] = None,
    attr_pool: Optional[List[str]] = None,
    string_pool: Optional[List[str]] = None,
    cdata_pool: Optional[List[str]] = None,
    comment_pool: Optional[List[str]] = None,
    text_pool: Optional[List[str]] = None,
) -> Tuple[str, bool]:

    tag_pool = tag_pool or []
    attr_pool = attr_pool or []
    string_pool = string_pool or []
    cdata_pool = cdata_pool or []
    comment_pool = comment_pool or []
    text_pool = text_pool or []
    
    stack: List[str] = []
    out_parts: List[str] = []
    i = 0
    n = len(tokens)

    while i < n:
        t = tokens[i]

        # ----------------------
        # Opening / closing tags
        # ----------------------
        if t == "<":
            next_tok = tokens[i+1] if i+1 < n else None
            if next_tok == "/":  # closing tag
                i += 2
                if i < n and tokens[i] == "Name":
                    name = stack.pop() if stack else pick_tag(tag_pool, context, rng)
                    out_parts.append(f"</{name}>")
                    i += 1
                    if i < n and i < n and tokens[i] == ">":
                        i += 1
                    continue
                else:
                    name = stack.pop() if stack else pick_tag(tag_pool, context, rng)
                    out_parts.append(f"</{name}>")
                    while i < n and tokens[i] != ">":
                        i += 1
                    if i < n and tokens[i] == ">":
                        i += 1
                    continue

            # opening tag
            i += 1
            if i < n and tokens[i] == "Name":
                prev_tag=stack[-1] if len(stack)>0 else None
                name = pick_tag(tag_pool, context, rng,prev_tag)
                stack.append(name)
                out_parts.append(f"<{name}")
                i += 1

                # Attributes
                seen_attrs = set()
                while i < n and tokens[i] not in {">", "/>"}:
                    if tokens[i] == "Name":
                        attr_name = pick_attr_for_tag(name, context, rng, fallback_pool=attr_pool, forbidden=seen_attrs)
                        seen_attrs.add(attr_name)
                        i += 1
                        if i < n and tokens[i] == "=":
                            i += 1
                        if i < n and i < n and tokens[i] == "STRING":
                            val = generate_attr_value(name, attr_name, string_pool, context, rng)
                            out_parts.append(f' {attr_name}="{val}"')
                            i += 1
                        else:
                            val = generate_attr_value(name, attr_name, string_pool, context, rng)
                            out_parts.append(f' {attr_name}="{val}"')
                    else:
                        i += 1

                # close tag
                if i < n and tokens[i] == "/>":
                    stack.pop()
                    out_parts.append(" />")
                    i += 1
                else:
                    if i < n and tokens[i] == ">":
                        out_parts.append(">")
                        i += 1
                    else:
                        out_parts.append(">")

                continue
            else:
                while i < n and tokens[i] != ">":
                    i += 1
                if i < n and tokens[i] == ">":
                    i += 1
                continue

        # ----------------------
        # Content tokens
        # ----------------------
        elif t == "TEXT":
            current_attribute = stack[-1] if stack else None
            current_tag = stack[-2] if len(stack)>=2 else None
            val = generate_text_for_tag(current_tag,current_attribute, context, rng, text_pool)
            out_parts.append(val)
            i += 1
            continue
        elif t.upper() == "CDATA":
            val = rng.choice(cdata_pool)
            val = generate_cdata_content(context,rng,cdata_pool)
            out_parts.append(f"<![CDATA[{val}]]>")
            i += 1
            continue
        elif t == "COMMENT":
            val = generate_random_comment(context, rng,fallback_pool=string_pool+comment_pool)
            out_parts.append(f"\n<!-- {val} -->\n")
            i += 1
            continue
        elif t == "EntityRef":
            val = generate_entity_ref_val(context,rng) # Random Name, could be anything
            out_parts.append(f"&{val};")
            i+=1
            continue
        elif t == "CharRef":
            val = generate_char_ref_text(rng)
            out_parts.append(val)
            i+=1
            continue
        elif t == "/":
            if stack:
                name = stack.pop()
                out_parts.append(f"</{name}>")
            i += 1
            if i < n and tokens[i] == "Name":
                i += 1
            if i < n and tokens[i] == ">":
                i += 1
            continue
        elif t in {">", "/>"}:
            out_parts.append(t)
            i += 1
            continue
        elif t == "STRING":
            out_parts.append(rng.choice(string_pool))
            i += 1
            continue
        else:
            if t in {"<", ">", "/>", "/", "="}:
                out_parts.append(t)
            i += 1
            continue

    # Close remaining open tags
    while stack:
        name = stack.pop()
        out_parts.append(f"</{name}>")

    xml_text = "".join(out_parts)
    xml_text = xml_text.replace(" >", ">").replace("< ", "<").replace("> <", "><")

    # Validate
    valid = True
    try:
        etree.fromstring(xml_text.encode("utf-8"))
    except Exception:
        valid = False

    return xml_text, valid

# ----------------------
# Automatic pool extraction
# ----------------------
def load_or_extract_pools(seeds_folder, top_k=200):
    """
    If corpus_paths exist, extract pools from files; otherwise, return empty dict.
    Returns a dict with keys: tag_pool, attr_pool, string_pool, cdata_pool, comment_pool, text_pool
    """
    if not seeds_folder:
        return {}

    # Run your existing extraction function
    pools = extract_pools_from_files(seeds_folder, top_k=top_k)

    # Keep only the pools relevant for concretizer
    merged_pools = {
        "tag_pool": pools.get("tag_pool", []),
        "attr_pool": pools.get("attr_pool", []),
        "string_pool": pools.get("string_pool", []),
        "cdata_pool": pools.get("cdata_pool", []),
        "comment_pool": pools.get("comment_pool", []),
        "text_pool": pools.get("text_pool", []),
    }
    return merged_pools

# ----------------------
# Helper to merge with defaults
# ----------------------
def merge_with_defaults(extracted: Dict[str,List[str]]):
    return {
        "tag_pool": extracted.get("tag_pool", []) + DEFAULT_TAG_NAMES,
        "attr_pool": extracted.get("attr_pool", []) + DEFAULT_ATTR_NAMES,
        "string_pool": extracted.get("string_pool", []) + DEFAULT_STRING_VALUES,
        "cdata_pool": extracted.get("cdata_pool", []) + DEFAULT_CDATA,
        "comment_pool": extracted.get("comment_pool", []) + DEFAULT_COMMENTS,
        "text_pool": extracted.get("text_pool", []) + DEFAULT_TEXT,
    }

# ----------------------
# Updated concretize_many_and_write
# ----------------------
def concretize_many_and_write(
    token_sequences: List[List[str]],
    out_folder: str,
    seeds_folder:str,
    batches:int = 20, 
    *,
    context: ConcretizerContext,
) -> Dict[str, Any]:
    os.makedirs(out_folder, exist_ok=True)

    # ----------------------
    # Load or extract pools
    # ----------------------
    extracted = load_or_extract_pools(seeds_folder)
    pools = merge_with_defaults(extracted)

    for i, seq in enumerate(token_sequences):
        for j in range(batches):
            index = i*batches+j
            rng_sample = random
            xml_text, valid = concretize_token_list(
                seq,
                context=context,
                rng=rng_sample,
                tag_pool=pools["tag_pool"],
                attr_pool=pools["attr_pool"],
                string_pool=pools["string_pool"],
                cdata_pool=pools["cdata_pool"],
                comment_pool=pools["comment_pool"],
                text_pool=pools["text_pool"],
            )
            fname = f"input_{index}.xml"
            fpath = os.path.join(out_folder, fname)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(xml_text)
    