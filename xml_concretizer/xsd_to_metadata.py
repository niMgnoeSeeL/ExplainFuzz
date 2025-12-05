"""
xsd_to_metadata.py

Parse one or more XSD files and produce a mapping:
{
  "request": {
      "user_id": "xs:long",
      "quota": "xs:long",
      ...
  },
  ...
}

Usage:
    metadata = parse_xsds_to_metadata(["schemas/request.xsd", "schemas/file.xsd"])
    import json
    print(json.dumps(metadata, indent=2))
    # or write to file
    with open("schema_metadata.json","w") as f:
        json.dump(metadata, f, indent=2)
"""

from xml.etree import ElementTree as ET
import json
from typing import Any, List, Dict,Tuple
import os

XSD_NS = "{http://www.w3.org/2001/XMLSchema}"

def _qn(local: str) -> str:
    return f"{XSD_NS}{local}"

def parse_xsds_to_metadata(xsd_paths: List[str]) -> Dict[str, Dict[str, str]]:
    """
    Parse XSD files and return a mapping:
        { element_name: { attribute_name: attribute_type, ... }, ... }

    Limitations:
      - Handles inline <xs:complexType> attributes, named <xs:complexType> referenced via 'type'
      - Handles <xs:attribute ref="..."> where ref refers to a global attribute defined in the set of input files
      - Handles simpleContent/extension that add attributes
      - Does NOT fully implement XSD import/include resolution across remote schemas
      - Does not expand attributeGroups or complex type inheritance beyond the same-file named complexType resolution
    """
    # 1) parse and collect tree objects
    trees = []
    for p in xsd_paths:
        trees.append(ET.parse(p).getroot())

    # 2) collect named complexTypes and global attributes across all provided XSDs
    complex_types = {}   # name -> complexType element
    global_attributes = {}  # name -> attribute element (type may be in 'type' attr)

    for root in trees:
        # collect named complexType
        for ct in root.findall(_qn("complexType")):
            name = ct.get("name")
            if name:
                complex_types[name] = ct
        # also complexType under schema: sometimes nested under other things; walk full tree
        for ct in root.findall(".//" + _qn("complexType")):
            name = ct.get("name")
            if name:
                complex_types[name] = ct
        # global attributes
        for ga in root.findall(_qn("attribute")):
            gname = ga.get("name")
            if gname:
                global_attributes[gname] = ga

    def _collect_subelements(ct_elem) -> List[str]:
        """Recursively collect all element names inside sequence/choice/all under a complexType."""
        names = []
        if ct_elem is None:
            return names
        # search recursively for all sequence/choice/all
        for seq_tag in ["sequence", "choice", "all"]:
            for seq in ct_elem.findall(".//" + _qn(seq_tag)):
                for subel in seq.findall(_qn("element")):
                    # handle 'name' or 'ref'
                    sname = subel.get("name")
                    sref = subel.get("ref")
                    if sname:
                        names.append(sname)
                    elif sref:
                        # take local part if namespaced
                        if ":" in sref:
                            _, local = sref.split(":", 1)
                        else:
                            local = sref
                        names.append(local)
                    # recursively check if the element has an inline complexType
                    sub_ct = subel.find(_qn("complexType"))
                    if sub_ct is not None:
                        names.extend(_collect_subelements(sub_ct))
        return names


    def _attrs_and_subelements_from_complexType(ct_elem) -> Dict[str, Any]:
        out_attrs = {}
        out_subelems = []

        if ct_elem is None:
            return {"attributes": out_attrs, "subelements": out_subelems}

        # 1) collect attributes
        for attr in ct_elem.findall(_qn("attribute")):
            aname = attr.get("name")
            aref = attr.get("ref")
            if aref:
                if ":" in aref:
                    _, local = aref.split(":", 1)
                    t = global_attributes.get(local, {}).get("type", "")
                else:
                    t = global_attributes.get(aref, {}).get("type", "")
                out_attrs[local if ":" in aref else aref] = t
                continue
            if aname:
                out_attrs[aname] = attr.get("type") or ""

        # 2) collect subelements recursively
        out_subelems.extend(_collect_subelements(ct_elem))

        # 3) simpleContent/extension attributes
        sc = ct_elem.find(_qn("simpleContent"))
        if sc is not None:
            ext = sc.find(_qn("extension"))
            if ext is not None:
                for attr in ext.findall(_qn("attribute")):
                    aname = attr.get("name") or attr.get("ref")
                    if aname:
                        out_attrs[aname] = attr.get("type") or ""

        # 4) attributeGroup handling (same as before)
        for agref in ct_elem.findall(_qn("attributeGroup")):
            ref = agref.get("ref")
            if ref:
                local = ref.split(":",1)[-1] if ":" in ref else ref
                for root in trees:
                    ag = root.find(_qn("attributeGroup") + f"[@name='{local}']")
                    if ag is not None:
                        for attr in ag.findall(_qn("attribute")):
                            name = attr.get("name")
                            if name:
                                out_attrs[name] = attr.get("type") or ""
                        break

        return {"attributes": out_attrs, "subelements": out_subelems}

    # element-level helper
    def _element_metadata(elem) -> Dict[str, Any]:
        meta = {"attributes": {}, "subelements": []}
        ct = elem.find(_qn("complexType"))
        if ct is not None:
            ct_meta = _attrs_and_subelements_from_complexType(ct)
            meta["attributes"].update(ct_meta["attributes"])
            meta["subelements"].extend(ct_meta["subelements"])
        # type reference to named complexType
        etype = elem.get("type")
        if etype:
            local = etype.split(":",1)[-1] if ":" in etype else etype
            if local in complex_types:
                ct_meta = _attrs_and_subelements_from_complexType(complex_types[local])
                meta["attributes"].update(ct_meta["attributes"])
                meta["subelements"].extend(ct_meta["subelements"])
        # attributes declared directly under element
        for a in elem.findall(_qn("attribute")):
            name = a.get("name") or a.get("ref")
            if name:
                meta["attributes"][name] = a.get("type") or ""
        return meta

    # collect all xs:element definitions
    result = {}
    for root in trees:
        for elem in root.findall(".//" + _qn("element")):
            ename = elem.get("name")
            if not ename or ename in result:
                continue
            result[ename] = _element_metadata(elem)
    return result

def get_metadata(schema_folder,file_save_metadata):
    metadata = {}
    # try:
    #     with open(file_save_metadata, "r") as f:
    #         metadata = json.load(f)
    #     if metadata:
    #         return metadata
    # except:
    #     pass
    
    paths = []
    for root, _, files in os.walk(schema_folder):
        for filename in files:
            if filename.endswith(".xsd"):
                file_path = os.path.join(root, filename)
                paths.append(file_path)
    metadata = parse_xsds_to_metadata(paths)
    with open(file_save_metadata, "w", encoding="utf-8") as fout:
        json.dump(metadata, fout, indent=2, ensure_ascii=False)
    print(f"Wrote metadata for {len(metadata)} elements to {file_save_metadata}")
    return metadata


def get_main_tags(metadata: Dict[str, Dict]) -> Tuple[Dict, Dict]:
    """
    Split tags into main_tags and secondary_tags.
    
    - main_tags: tags with at least one attribute or subelement
    """
    main_tags = {}
    
    for tag, info in metadata.items():
        attrs = info.get("attributes", {})
        subs = info.get("subelements", [])
        if attrs or subs:
            main_tags[tag] = info
            
    return main_tags

# -- Example usage --
if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Parse XSD(s) and export element->attribute->type metadata JSON.")
    # parser.add_argument("xsd_files", nargs="+", help="One or more XSD files or glob (space-separated).")
    # parser.add_argument("--out", "-o", default="schema_metadata.json", help="Output JSON path.")
    # args = parser.parse_args()

    # # expand globs if needed (Path.glob not used here; assume explicit files)
    # paths = []
    # for p in args.xsd_files:
    #     # allow directories
    #     pp = Path(p)
    #     if pp.is_dir():
    #         for f in pp.glob("*.xsd"):
    #             paths.append(str(f))
    #     else:
    #         paths.append(p)
    # paths = ["xml_concretizer/auth_service_xml/config/user.xsd","xml_concretizer/auth_service_xml/config/file.xsd","xml_concretizer/auth_service_xml/config/request.xsd","xml_concretizer/auth_service_xml/config/query.xsd"]
    # metadata = parse_xsds_to_metadata(paths)
    file_save_metadata = "xml_concretizer/out/metadata.json"
    schema_folder = "xml_concretizer/auth_service_xml/config/"
    metadata = get_metadata(schema_folder,file_save_metadata)
    # with open("xml_concretizer/metadata.json", "w", encoding="utf-8") as fout:
    #     json.dump(metadata, fout, indent=2, ensure_ascii=False)
    print(f"Wrote metadata for {len(metadata)} elements to xml_concretizer/out/metadata.json")
