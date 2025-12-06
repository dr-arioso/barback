
# Build Pipeline Lifecycle

The lifecycle consists of six deterministic phases:

## 1. Discovery
- Locate Booster Pack root
- Load `booster.yaml`
- Identify all subfolders (`dex/`, `tags/`, `skills/`, etc.)

## 2. Schema Validation
- Validate each YAML file against its schema:
  - taxonomy schema  
  - tag schema  
  - skill/resolver/pipeline config schemas  
- Fail early on structural errors

## 3. DexTree Compilation
- Build DexNodes from taxonomy YAML files
- Check for:
  - cycles  
  - missing parents  
  - duplicate node names  
- Produce runtime DexTree and lineage tables

## 4. Tag Compilation
- Normalize tag identifiers
- Validate mapping to DexNodes (if required)
- Generate inverted indices for quick lookup

## 5. Configuration Merge
- Merge pack-level defaults into StashKit’s global config
- Resolve conflicts using standard precedence rules

## 6. Artifact Packaging
- Produce outputs:
  - compiled taxonomy (.json)
  - compiled tag maps
  - packed config
  - loader/manifest
- Cache artifacts for fast runtime loading
