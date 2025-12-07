import json
import hashlib
import time
from pathlib import Path
from typing import Dict, Any, List

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


ALLOWED_TYPES = {
    "system",
    "subsystem",
    "concept",
    "component",
    "process",
    "rule",
    "term",
}

ALLOWED_REL_TYPES = {
    "uses",
    "extends",
    "contains",
    "produces",
    "updates",
    "depends_on",
    "may_include",
    "implements",
    "enriches",
    "builds",
}


def load_yaml_files(root: Path) -> List[Dict[str, Any]]:
    if yaml is None:
        raise RuntimeError("PyYAML is required to compile the MetaDex.")
    data: List[Dict[str, Any]] = []
    for path in sorted(root.rglob("*.yml")):
        obj = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        obj["_source_path"] = str(path)
        data.append(obj)
    return data


def normalize_value(value: Any, in_api: bool = False) -> Any:
    """Normalize YAML-loaded values into a predictable, ML-friendly shape.

    - Outside `api`, lists of single-key dicts are collapsed to "key: value" strings.
    - Inside `api`, dicts are preserved to avoid breaking method/property definitions.
    """
    if isinstance(value, dict):
        return {
            k: normalize_value(v, in_api=in_api or (k == "api"))
            for k, v in value.items()
        }

    if isinstance(value, list):
        normalized_list = []
        for item in value:
            if isinstance(item, dict) and not in_api:
                if len(item) == 1:
                    k, v = next(iter(item.items()))
                    normalized_list.append(f"{k}: {v}")
                else:
                    normalized_list.append({
                        k: normalize_value(v, in_api=in_api)
                        for k, v in item.items()
                    })
            else:
                normalized_list.append(normalize_value(item, in_api=in_api))
        return normalized_list

    return value


def validate_entities(entities: Dict[str, Dict[str, Any]]):
    for ent_id, ent in entities.items():
        for key in ("id", "name", "type", "description"):
            if key not in ent:
                raise ValueError(f"Entity {ent_id} missing required key: {key}")
        if ent["type"] not in ALLOWED_TYPES:
            raise ValueError(f"Entity {ent_id} has invalid type: {ent['type']}")

        api = ent.get("api")
        if api is not None and not isinstance(api, dict):
            raise ValueError(f"Entity {ent_id} api must be a dict if present.")
        if isinstance(api, dict):
            for section in ("public_methods", "internal_methods", "properties", "events"):
                if section in api and not isinstance(api[section], list):
                    raise ValueError(
                        f"Entity {ent_id} api.{section} must be a list."
                    )


def validate_relationships(rels: List[Dict[str, Any]], entities: Dict[str, Dict[str, Any]]):
    for rel in rels:
        if rel["type"] not in ALLOWED_REL_TYPES:
            raise ValueError(f"Invalid relationship type: {rel['type']}")
        if rel["from"] not in entities:
            raise ValueError(f"Relationship from unknown entity: {rel['from']}")
        if rel["to"] not in entities:
            raise ValueError(f"Relationship to unknown entity: {rel['to']}")


def build_entities(source_dir: Path) -> Dict[str, Dict[str, Any]]:
    entities: Dict[str, Dict[str, Any]] = {}

    core_dir = source_dir / "core"
    subsystems_dir = source_dir / "subsystems"
    terminology_dir = source_dir / "terminology"

    for section_dir in (core_dir, subsystems_dir, terminology_dir):
        if not section_dir.exists():
            continue
        for obj in load_yaml_files(section_dir):
            if "id" not in obj:
                raise ValueError(f"Entity file missing id: {obj.get('_source_path')}")
            ent_id = obj["id"]
            if ent_id in entities:
                raise ValueError(f"Duplicate entity id: {ent_id}")
            obj.pop("_source_path", None)
            normalized = normalize_value(obj)
            entities[ent_id] = normalized

    validate_entities(entities)
    return entities


def build_relationships(source_dir: Path, entities: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    rels: List[Dict[str, Any]] = []
    rel_dir = source_dir / "relationships"
    if rel_dir.exists():
        for obj in load_yaml_files(rel_dir):
            if "relationships" not in obj:
                continue
            for r in obj["relationships"]:
                rels.append({
                    "from": r["from"],
                    "type": r["type"],
                    "to": r["to"],
                })
    validate_relationships(rels, entities)
    return rels


def load_rules(source_dir: Path) -> List[Dict[str, Any]]:
    rules_dir = source_dir / "rules"
    rules: List[Dict[str, Any]] = []
    if not rules_dir.exists():
        return rules
    for obj in load_yaml_files(rules_dir):
        if "rules" in obj:
            for r in obj["rules"]:
                r.pop("_source_path", None)
                rules.append(r)
    return rules


def apply_simple_trait_propagation(entities: Dict[str, Dict[str, Any]], rules: List[Dict[str, Any]]):
    for rule in rules:
        if rule.get("rule_type") != "trait_propagation":
            continue
        for logic in rule.get("logic", []):
            system_id = logic.get("when_system_id")
            if not system_id or system_id not in entities:
                continue
            traits_to_prop = logic.get("propagate_traits", {}).get("traits", [])
            targets = logic.get("propagate_traits", {}).get("to", [])
            for target_id in targets:
                if target_id not in entities:
                    continue
                ent = entities[target_id]
                ent_traits = ent.setdefault("traits", [])
                for t in traits_to_prop:
                    if t not in ent_traits:
                        ent_traits.append(t)


def build_reverse_relationships(relationships: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    rev: Dict[str, List[Dict[str, Any]]] = {}
    for r in relationships:
        tgt = r["to"]
        rev.setdefault(tgt, []).append({
            "from": r["from"],
            "type": r["type"],
        })
    return rev


def compute_source_hash(source_dir: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(source_dir.rglob("*.yml")):
        h.update(str(path).encode("utf-8"))
        with path.open("rb") as f:
            h.update(f.read())
    return "sha256:" + h.hexdigest()


def compile_metadex(source_dir: str, output_file: str) -> None:
    src = Path(source_dir)
    if not src.exists():
        raise ValueError(f"Source directory does not exist: {src}")

    entities = build_entities(src)
    relationships = build_relationships(src, entities)
    rules = load_rules(src)

    apply_simple_trait_propagation(entities, rules)

    derived = {
        "reverse_relationships": build_reverse_relationships(relationships),
    }

    version_info = {
        "version": "1.2.0",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_hash": compute_source_hash(src),
        "compiler_version": "1.2",
        "schema_version": "2025-01",
    }

    metadex = {
        "entities": entities,
        "relationships": relationships,
        "rules": rules,
        "derived": derived,
        "version_info": version_info,
    }

    out_path = Path(output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(metadex, indent=2, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Compile StashKit MetaDex (v1.2 with YAML normalization)")
    parser.add_argument("--source", default="source_yaml", help="Source YAML directory")
    parser.add_argument("--output", default="metadex/metadex.json", help="Output JSON file")
    args = parser.parse_args()
    compile_metadex(args.source, args.output)
