
# TagPack Template

## Overview
A TagPack provides metadata overlays (StashTags) for DexNodes.

## Directory Structure
```
tagpack-example/
  booster.yaml
  tags/
    legal.yaml
    production.yaml
```

## booster.yaml
```yaml
name: tagpack-example
version: 0.1.0
type: tagpacks
description: "Example TagPack"
entry_points:
  tags: tags/
dependencies: []
```

## tags/legal.yaml
```yaml
root_category.subcategory:
  class: "Example Class"
  type: "Example Type"
```

## Notes
- Keys must match canonical DexPack paths.
