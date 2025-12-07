#!/usr/bin/env python3
"""
MetaDex compiler v2.0 (for MetaDex 1.3+)

- Loads entities from source_yaml/core, source_yaml/subsystems, source_yaml/terminology
- Loads relationships from source_yaml/relationships
- Loads rules from source_yaml/rules
- Validates structure and types
- Reads VERSION dynamically
- Writes a single metadex.json file

Usage:
    python compiler.py --source source_yaml --output metadex/metadex.json [--minify]

This compiler intentionally does NOT support the old 1.2 schema.
"""

import argparse
import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple

import yaml


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"ERROR: Required file not found: {path}")


def load_yaml_file(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"ERROR: YAML file not found: {path}")
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as e:
        raise SystemExit(f"ERROR: Failed to parse YAML: {path}\n{e}")


def sha256_of_files(paths: List[Path]) -> str:
    h = hashlib.sha256()
    for p in sorted(paths, key=lambda x: str(x)):
        h.update(str(p).encode("utf-8"))
        h.update(b"\n")
        h.update(p.read_bytes())
        h.update(b"\n")
    return "sha256:" + h.hexdigest()


# ---------------------------------------------------------------------------
# Schema validation
# ---------------------------------------------------------------------------

ALLOWED_ENTITY_TYPES = {"system", "subsystem", "concept"}


def validate_entity(entity: Dict[str, Any], source_file: Path) -> None:
    """Validate a single entity object against the v1.3 MetaDex schema."""
    required_keys = ("id", "name", "type", "description")
    for k in required_keys:
        if k not in entity:
            raise SystemExit(
                f"ERROR in {source_file}: entity is missing required field '{k}'."
            )

    etype = entity["type"]
    if etype not in ALLOWED_ENTITY_TYPES:
        raise SystemExit(
            f"ERROR in {source_file}: entity type '{etype}' is not allowed. "
            f"Expected one of {sorted(ALLOWED_ENTITY_TYPES)}."
        )

    # Traits should be a list if present
    if "traits" in entity and not isinstance(entity["traits"], list):
        raise SystemExit(
            f"ERROR in {source_file}: 'traits' must be a list if present."
        )

    # fields should be a dict if present
    if "fields" in entity and not isinstance(entity["fields"], dict):
        raise SystemExit(
            f"ERROR in {source_file}: 'fields' must be a mapping/dict if present."
        )

    # api validation
    if "api" in entity:
        api = entity["api"]
        if not isinstance(api, dict):
            raise SystemExit(
                f"ERROR in {source_file}: 'api' must be a mapping/dict when present."
            )
        validate_api(api, source_file)


def validate_api(api: Dict[str, Any], source_file: Path) -> None:
    """Validate the api block of an entity."""
    # Each section is either absent or a list
    sections = ("public_methods", "internal_methods", "properties", "events")
    for sec in sections:
        if sec in api:
            if not isinstance(api[sec], list):
                raise SystemExit(
                    f"ERROR in {source_file}: api['{sec}'] must be a list."
                )
            if sec in ("public_methods", "internal_methods"):
                for method in api[sec]:
                    validate_method(method, source_file, sec)
            elif sec == "properties":
                for prop in api[sec]:
                    validate_property(prop, source_file)
            elif sec == "events":
                for ev in api[sec]:
                    validate_event(ev, source_file)


def validate_method(method: Dict[str, Any], source_file: Path, section: str) -> None:
    if not isinstance(method, dict):
        raise SystemExit(
            f"ERROR in {source_file}: methods in '{section}' must be mappings."
        )
    if "name" not in method:
        raise SystemExit(
            f"ERROR in {source_file}: a method in '{section}' is missing 'name'."
        )
    # description is strongly recommended
    if "description" in method and not isinstance(method["description"], str):
        raise SystemExit(
            f"ERROR in {source_file}: method '{method['name']}' description must be a string."
        )
    if "params" in method and not isinstance(method["params"], list):
        raise SystemExit(
            f"ERROR in {source_file}: method '{method['name']}' params must be a list when present."
        )


def validate_property(prop: Dict[str, Any], source_file: Path) -> None:
    if not isinstance(prop, dict):
        raise SystemExit(
            f"ERROR in {source_file}: properties entries must be mappings."
        )
    if "name" not in prop:
        raise SystemExit(
            f"ERROR in {source_file}: a property is missing 'name'."
        )


def validate_event(ev: Dict[str, Any], source_file: Path) -> None:
    if not isinstance(ev, dict):
        raise SystemExit(
            f"ERROR in {source_file}: events entries must be mappings."
        )
    if "name" not in ev:
        raise SystemExit(
            f"ERROR in {source_file}: an event is missing 'name'."
        )


def validate_relationships(
    relationships: List[Dict[str, Any]], entity_ids: List[str], source_file: Path
) -> None:
    for rel in relationships:
        if not isinstance(rel, dict):
            raise SystemExit(
                f"ERROR in {source_file}: each relationship must be a mapping."
            )
        for field in ("from", "to", "type"):
            if field not in rel:
                raise SystemExit(
                    f"ERROR in {source_file}: relationship missing '{field}'."
                )
        if rel["from"] not in entity_ids:
            raise SystemExit(
                f"ERROR: relationship 'from' references unknown id '{rel['from']}'."
            )
        if rel["to"] not in entity_ids:
            raise SystemExit(
                f"ERROR: relationship 'to' references unknown id '{rel['to']}'."
            )


def validate_rules(rules: List[Dict[str, Any]], source_file: Path) -> None:
    for rule in rules:
        if not isinstance(rule, dict):
            raise SystemExit(
                f"ERROR in {source_file}: each rule must be a mapping."
            )
        if "id" not in rule:
            raise SystemExit(
                f"ERROR in {source_file}: rule missing 'id'."
            )
        if "rule_type" not in rule:
            raise SystemExit(
                f"ERROR in {source_file}: rule '{rule['id']}' missing 'rule_type'."
            )
        if "logic" not in rule:
            raise SystemExit(
                f"ERROR in {source_file}: rule '{rule['id']}' missing 'logic'."
            )
        if not isinstance(rule["logic"], list):
            raise SystemExit(
                f"ERROR in {source_file}: rule '{rule['id']}' logic must be a list."
            )


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------

def load_entities(source_dir: Path) -> Tuple[Dict[str, Dict[str, Any]], List[Path]]:
    """
    Load entities from:
        source_yaml/core
        source_yaml/subsystems
        source_yaml/terminology
    """
    entities: Dict[str, Dict[str, Any]] = {}
    yaml_files: List[Path] = []

    for subdir_name in ("core", "subsystems", "terminology"):
        subdir = source_dir / subdir_name
        if not subdir.is_dir():
            continue
        for path in sorted(subdir.rglob("*.yml")):
            yaml_files.append(path)
            obj = load_yaml_file(path)
            if not isinstance(obj, dict):
                raise SystemExit(f"ERROR in {path}: top-level YAML must be a mapping.")
            # Expect a single entity per file
            if "id" not in obj:
                raise SystemExit(f"ERROR in {path}: missing top-level 'id' field.")
            entity_id = obj["id"]
            if entity_id in entities:
                raise SystemExit(
                    f"ERROR: duplicate entity id '{entity_id}' in {path} "
                    f"(already defined in another file)."
                )
            validate_entity(obj, path)
            entities[entity_id] = obj

    if not entities:
        raise SystemExit("ERROR: No entities loaded from 'core', 'subsystems', or 'terminology'.")

    return entities, yaml_files


def load_relationships(source_dir: Path) -> Tuple[List[Dict[str, Any]], List[Path]]:
    rel_dir = source_dir / "relationships"
    relationships: List[Dict[str, Any]] = []
    paths: List[Path] = []

    if not rel_dir.is_dir():
        return relationships, paths

    for path in sorted(rel_dir.rglob("*.yml")):
        obj = load_yaml_file(path)
        if not isinstance(obj, dict) or "relationships" not in obj:
            continue
        rels = obj["relationships"]
        if not isinstance(rels, list):
            raise SystemExit(
                f"ERROR in {path}: 'relationships' must be a list."
            )
        relationships.extend(rels)
        paths.append(path)

    return relationships, paths


def load_rules(source_dir: Path) -> Tuple[List[Dict[str, Any]], List[Path]]:
    rules_dir = source_dir / "rules"
    rules: List[Dict[str, Any]] = []
    paths: List[Path] = []

    if not rules_dir.is_dir():
        return rules, paths

    for path in sorted(rules_dir.rglob("*.yml")):
        obj = load_yaml_file(path)
        if not isinstance(obj, dict) or "rules" not in obj:
            continue
        rules_list = obj["rules"]
        if not isinstance(rules_list, list):
            raise SystemExit(
                f"ERROR in {path}: 'rules' must be a list."
            )
        rules.extend(rules_list)
        paths.append(path)

    return rules, paths


def load_version_info(repo_root: Path, source_paths: List[Path]) -> Dict[str, Any]:
    version_file = repo_root / "VERSION"
    try:
        version = version_file.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        version = "0.0.0"

    timestamp = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    source_hash = sha256_of_files(source_paths)

    return {
        "version": version,
        "schema_version": "2025-12",
        "compiler_version": "2.0",
        "source_hash": source_hash,
        "timestamp": timestamp,
    }


# ---------------------------------------------------------------------------
# Main compile function
# ---------------------------------------------------------------------------

def compile_metadex(source_dir: Path, output_path: Path, minify: bool = False) -> None:
    repo_root = source_dir.parent  # assumes source_yaml/ at repo root

    entities, entity_yaml_files = load_entities(source_dir)
    relationships, rel_yaml_files = load_relationships(source_dir)
    rules, rule_yaml_files = load_rules(source_dir)

    # Validate relationships and rules with entity ids
    entity_ids = list(entities.keys())
    for path in rel_yaml_files:
        validate_relationships(relationships, entity_ids, path)
    for path in rule_yaml_files:
        validate_rules(rules, path)

    # Build version info with hash over all YAML files
    all_yaml_files = entity_yaml_files + rel_yaml_files + rule_yaml_files
    version_info = load_version_info(repo_root, all_yaml_files)

    metadex = {
        "version_info": version_info,
        "entities": entities,
        "relationships": relationships,
        "rules": rules,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if minify:
        json_text = json.dumps(metadex, separators=(",", ":"), ensure_ascii=False)
    else:
        json_text = json.dumps(metadex, indent=2, ensure_ascii=False)

    output_path.write_text(json_text, encoding="utf-8")
    print(f"Wrote MetaDex to {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: List[str]) -> None:
    parser = argparse.ArgumentParser(description="Compile MetaDex YAML into JSON.")
    parser.add_argument(
        "--source",
        type=str,
        default="source_yaml",
        help="Path to the source_yaml directory (default: source_yaml)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="metadex/metadex.json",
        help="Path to output JSON file (default: metadex/metadex.json)",
    )
    parser.add_argument(
        "--minify",
        action="store_true",
        help="Write minified JSON instead of pretty-printed.",
    )

    args = parser.parse_args(argv)

    source_dir = Path(args.source).resolve()
    output_path = Path(args.output).resolve()

    if not source_dir.is_dir():
        raise SystemExit(f"ERROR: Source directory not found: {source_dir}")

    compile_metadex(source_dir, output_path, minify=args.minify)


if __name__ == "__main__":
    main(sys.argv[1:])
