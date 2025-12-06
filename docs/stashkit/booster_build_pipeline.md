
# StashKit Booster Build Pipeline Guide

This document details the generalized build pipeline for all StashKit Booster Packs:
DexPacks, TagPacks, SkillsPacks, ResolverPacks, and StashPacks.

## 1. Overview

A BoosterPack extends StashKit by providing:
- Taxonomy trees (DexPacks)
- Metadata overlays (TagPacks)
- Skills (SkillsPacks)
- Resolvers (ResolverPacks)
- Complete domain bundles (StashPacks)

BoosterPacks have a shared structure and lifecycle:
1. Manifest Loading
2. Resource Discovery
3. Dependency Resolution
4. Build / Compilation (DexPacks + TagPacks)
5. Registration (Skills, Resolvers)
6. Final Assembly (StashPack)

---

## 2. BoosterPack Manifest

Each pack includes `booster.yaml`:

```yaml
name: boozedex
version: 1.0.0
type: dexpacks
entry_points:
  taxonomy: taxonomy/
  compiled: compiled/boozedex.json
dependencies:
  - tagpack-ttb
```

Required keys:
- `name`
- `version`
- `type`
- `entry_points`

Optional:
- `dependencies`
- `description`
- `stability`

---

## 3. BoosterPack Types

### 3.1 DexPack
Contains:
- YAML taxonomy trees
- Optional compiled JSON
- Optional overlays

Build step:
- Merge taxonomies
- Apply overlays
- Validate using JSON Schema
- Export `nodes`, `aliases`, `roles`, `metadata_index`

### 3.2 TagPack
Contains:
- YAML metadata overlays
- Role tables
- Alias tables

Merged onto DexPacks during build.

### 3.3 SkillsPack
Contains:
- Python Skills classes
- Optional config templates
- Optional data helpers

Registered via StashKit Skills loader.

### 3.4 ResolverPack
Contains:
- Resolver classes
- Optional resolver config

Registered via StashKit Resolver loader.

### 3.5 StashPack
Combines multiple BoosterPacks into a domain-specific bundle.

---

## 4. Build Pipeline in Detail

### Step 1: Load Manifest
The loader reads `booster.yaml` and identifies:
- pack type
- dependencies
- filesystem layout

### Step 2: Resolve Dependencies
StashKit builds a dependency graph:
- Verifies no cycles
- Enforces load ordering:
  1. DexPacks
  2. TagPacks
  3. SkillsPacks
  4. ResolverPacks
  5. StashPacks

### Step 3: Discover Resources
Load:
- taxonomy YAML
- overlays
- skill modules
- resolver modules
- metadata files

### Step 4: Compile (DexPack + TagPack only)
DexPack compilation:
- Merge YAML trees
- Build DexNodes
- Compute paths & ancestors
- Apply TagPack metadata
- Build indices
- Generate version hash
- Validate via schema

### Step 5: Register (SkillsPack + ResolverPack)
Skills:
- Added to global Skills registry

Resolvers:
- Added to Resolver registry
- Exposed for pipelines

### Step 6: Assemble StashPack
Final pack includes:
- DexPack outputs
- TagPack metadata
- Skills
- Resolvers
- Domain config

---

## 5. Developer Workflow

### Creating a DexPack
1. Add taxonomy YAML
2. Add overlays
3. Add `booster.yaml`
4. Run compiler
5. Validate schema

### Creating a TagPack
1. Add metadata files
2. Add `booster.yaml`
3. Validate keys match DexPack paths

### Creating a SkillsPack
1. Add skill modules
2. Add Skill registration
3. Add `booster.yaml`

### Creating a ResolverPack
1. Implement resolvers
2. Register via manifest

### Creating a StashPack
1. Combine all boosters
2. Provide sample configs
3. Provide domain helpers

---

## 6. File Layout Templates

### DexPack
```
boozedex/
  booster.yaml
  taxonomy/
  overlays/
  compiled/
```

### TagPack
```
tagpack-ttb/
  booster.yaml
  tags/
```

### SkillsPack
```
skillspack-vision/
  booster.yaml
  skills/
```

### ResolverPack
```
resolverpack-barback/
  booster.yaml
  resolvers/
```

### StashPack
```
stashpack-barback/
  booster.yaml
  dependencies/
  config/
```

---

## 7. Build Outputs

All DexPack compilers produce:

```
boozedex.json
category_index.json
alias_index.json
role_index.json
metadata_index.json
boozedex_version.json
```

These are consumed by StashKit at runtime.

---

## 8. Summary

The StashKit Booster system:
- cleanly separates domain knowledge from core logic
- supports unlimited expansions
- ensures reproducible, validated builds
- maintains clean modular boundaries
- supports Barback and future apps with minimal coupling
