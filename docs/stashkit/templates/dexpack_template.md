
# DexPack Template

## Overview
A DexPack defines hierarchical taxonomies for StashKit. This template demonstrates the recommended structure for a new DexPack.

## Directory Structure
```
mypack/
  booster.yaml
  taxonomy/
    00_roots.yaml
    10_category.yaml
  overlays/
    aliases.yaml
    roles.yaml
  compiled/
```

## booster.yaml
```yaml
name: mypack
version: 0.1.0
type: dexpacks
description: "Example DexPack"
entry_points:
  taxonomy: taxonomy/
  compiled: compiled/mypack.json
dependencies: []
```

## taxonomy/00_roots.yaml
```yaml
root_category: {}
```

## overlays/aliases.yaml
```yaml
alias_name:
  - root_category.subcategory
```

## Notes
- After defining YAML, run the DexPack compiler.
- Validate compiled JSON against the DexPack schema.
