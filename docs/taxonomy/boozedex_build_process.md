
# BoozeDex Build Process Guide
This document describes how BoozeDex, a DexPack taxonomy, is transformed from human-maintained YAML sources into compiled JSON artifacts consumed by StashKit and StashPacks like Barback.

## 1. Overview
The build process converts:
- YAML taxonomy files
- TagPack overlays
- Metadata attachments

into:
- canonical JSON taxonomy
- lookup indices
- merged metadata
- reproducible version stamp

## 2. Directory Layout
```
boozedex/
  taxonomy/
    00_roots.yaml
    ...
  overlays/
    aliases.yaml
    roles.yaml
    ...
  build/
    boozedex.json
    category_index.json
    alias_index.json
    role_index.json
    metadata_index.json
    boozedex_version.json
  compile_boozedex.py
```

## 3. Build Steps

### 3.1 Load YAML
Files in `taxonomy/` are loaded in lexical order:
- 00_roots.yaml
- 10_spirits.yaml
- ...

Data is merged into a single nested dict.

### 3.2 Normalize Hierarchy
Each category becomes a DexNode with:
- path
- name
- children
- ancestors
- metadata

### 3.3 Apply Overlays
Overlays attach StashTags:
- aliases
- roles
- metadata groups (legal, regional, gs1, production, flavor)

### 3.4 Generate Indices
Compiler builds:
- category_index.json
- alias_index.json
- role_index.json
- metadata_index.json

### 3.5 Write Outputs
All artifacts saved in `build/`.

## 4. Versioning
A reproducible hash covers all YAML inputs.

## 5. Developer Workflow

### Edit Taxonomy
Modify YAML under `taxonomy/`.

### Add Metadata
Create/update files under `overlays/`.

### Compile
Run:
```
python compile_boozedex.py
```

### Validate
Use boozedex.schema.json to validate build output.

## 6. Integration with StashKit
Compiled JSON artifacts are loaded via DexPack loader.

## 7. Summary
BoozeDex compilation transforms rich YAML sources into efficient runtime JSON structures suitable for fast classification, search, and semantic reasoning.
