
# StashKit BoosterPack Architecture Overview

This document describes the full architecture, philosophy, and structure of the StashKit BoosterPack system, including DexPacks, TagPacks, SkillsPacks, ResolverPacks, and StashPacks, along with the concept of StashTags (metadata primitives).

## 1. Core Philosophy

StashKit is intentionally lightweight. It provides:
- A flexible Stash model
- A resolution pipeline
- Skills and resolvers
- Datastores and connectors

**But it does NOT embed domain-specific knowledge.**

Instead, StashKit loads optional expansions called **Booster Packs**, which can contribute:
- Taxonomies
- Metadata overlays
- Skills
- Resolvers
- Domain logic
- Configuration templates

This modular system allows Barback and any future vertical apps to reuse the same underlying machinery.

---

## 2. Booster Pack Types

StashKit defines several different pack types:

### 2.1 DexPack
A **DexPack** is a taxonomy pack.

It contains:
- One or more YAML classification trees
- Optional polyhierarchy rules
- Optional metadata overlays attached to the tree
- Optional compiled JSON for runtime

Examples:
- `boozedex` (alcohol taxonomy)
- `kitchendex`
- `plantdex`

DexPacks define **structure**: categories, parent–child relationships, topologies.

---

### 2.2 TagPack
A **TagPack** provides metadata overlays.

TagPacks define **StashTags**, which attach to DexNodes.

These include:
- Roles (cocktail roles, beverage roles)
- Legal statuses (TTB Class/Type, EU PDO/PGI)
- Production metadata
- Region/origin metadata
- Flavor profiles
- GS1 Bricks
- ABV ranges
- Numeric attributes
- Flags, annotations, aliases

Examples:
- `tagpack-ttb`
- `tagpack-cocktailroles`
- `tagpack-gs1`
- `tagpack-flavor`

---

### 2.3 SkillsPack
A **SkillsPack** provides reusable Skills.

Examples:
- `vision-basic` (OpenAI Vision, OCR skills)
- `vision-google`
- `upc-basic`
- `manual-entry-extensions`
- `nlp-summarization`

A SkillsPack may include:
- Python modules
- Example configuration
- Optional metadata
- Optional testing utilities

---

### 2.4 ResolverPack
A **ResolverPack** supplies domain-specific Resolver implementations.

Examples:
- `resolverpack-barback`
- `resolverpack-food`
- `resolverpack-plants`

Resolvers orchestrate:
- Skills
- Pipelines
- StashKit inference features
- Conflict resolution logic

---

### 2.5 StashPack
A **StashPack** is the complete domain bundle.

It combines:
- One or more DexPacks
- One or more TagPacks
- One or more SkillsPacks
- One ResolverPack
- Optional datastore presets
- Optional configuration
- Domain examples and helper utilities

Examples:
- `stashpack-barback`
- `stashpack-kitchen`
- `stashpack-garden`

A StashPack is essentially a “vertical extension.”

---

## 3. StashTags

StashTags are the **fundamental metadata unit** in StashKit.

Each StashTag has:
- a namespace (e.g., `legal`, `roles`, `flavor`)
- a name
- a value
- an optional confidence

StashTags attach to:
- DexNodes (categories)
- Stash items (inventory entries)
- Resolution results

Examples:
- `role: base_spirit`
- `legal.ttb.class: "Whiskey"`
- `flavor.citrus: high`
- `origin.country: Japan`

A **TagPack** is simply a bundle distributing StashTags.

---

## 4. Loader Architecture

Loaders in StashKit follow a layered approach:

1. Load all DexPacks → merge into a unified DexGraph
2. Load all TagPacks → merge StashTags onto DexNodes
3. Load all SkillsPacks → register Skills
4. Load all ResolverPacks → register Resolvers
5. Load StashPacks → apply preset configuration

Each step uses:
- stable ordering
- deterministic merges
- conflict reporting

---

## 5. Booster Manifest Format

Every pack includes a `booster.yaml` manifest:

```yaml
name: boozedex
version: 1.0.0
type: dexpacks
description: Alcohol classification tree + overlays

entry_points:
  taxonomy: taxonomy/
  compiled: compiled/boozedex.json

dependencies:
  - tagpack-ttb
  - tagpack-cocktailroles
```

StashKit uses this to:
- locate YAML files
- identify pack type
- know how to build/merge the pack
- track dependency relationships

---

## 6. Directory Structure

Example DexPack:

```
boozedex/
  booster.yaml
  taxonomy/
    00_roots.yaml
    10_spirits.yaml
    ...
  overlays/
    production_metadata.yaml
    ...
  compiled/
    boozedex.json
```

Example TagPack:

```
tagpack-ttb/
  booster.yaml
  tags/
    ttb_metadata.yaml
```

StashPack:

```
stashpack-barback/
  booster.yaml
  dependencies:
    - boozedex
    - tagpack-cocktailroles
    - resolverpack-barback
```

---

## 7. Current Implemented Drafts

This document corresponds to the early formation of:
- BoozeDex (DexPack)
- TagPack design (StashTags)
- StashPack (future Barback)
- compile_boozedex.py (compiler prototype)

This BoosterPack architecture becomes the backbone of StashKit extensibility.

---

## 8. Future Work

- Generalized BoosterCompiler for all DexPacks
- Booster registry system
- Packaging as pip installable packs
- Validation and static checking
- Booster dependency graph resolver
- StashPack deployment templates

---

## 9. Summary

StashKit’s BoosterPack architecture defines:

- **DexPack** → Taxonomies  
- **TagPack** → Metadata overlays (StashTags)  
- **SkillsPack** → Skills  
- **ResolverPack** → Resolvers  
- **StashPack** → Full-domain packs  

This framework allows:
- Infinite domain expansion  
- Clean modular organization  
- Stable core with powerful extensions  
- Reusability across projects  

It sets the stage for Barback and other apps built on StashKit.
