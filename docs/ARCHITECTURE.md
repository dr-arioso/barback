# Architecture Overview

This document describes the structure of the Barback + StashKit architecture.

---

## High-Level System Architecture

```mermaid
graph TD
  subgraph StashKit
    models[Models (Item, Product)]
    stash[Stash (container)]
    resolvers[Resolvers + StashSkills]
    source[StashSource (knowledge)]
    stores[DataStores]
    ontology[Ontology Engine]
  end

  subgraph Barback
    bottle[Bottle Model]
    bstash[BottleStash]
    bsource[BarbackStashSource]
    bresolver[BottleResolver]
    cli[barback.py (CLI)]
  end

  resolvers --> source
  source --> stores
  source --> ontology

  bresolver --> bsource
  bresolver --> bottle
  bottle --> bstash

  cli --> bresolver
  cli --> bstash
```

StashKit is the **framework**; Barback is a **client application** that:

- Defines its own domain-specific models (Bottle)
- Implements a BarbackStashSource backed by spirits ontology and brand data
- Uses StashSkills to enrich and normalize bottle metadata

---

## Resolver Pipeline

All resolvers follow the same high-level flow:

```mermaid
flowchart TD
  A[Start Resolution] --> B[Create ResolutionContext]
  B --> C{UPC available?}
  C -->|Yes| D[UPCSkill]
  C -->|No| E

  D --> F[DBLookupSkill]
  F --> E{Image available?}

  E -->|Yes| G[AIVisionSkill]
  E -->|No| H[Skip AIVision]

  G --> H[Manual/KeyboardEntrySkill]

  H --> I[BrandSkill / CategorySkill / VolumeSkill / DimensionSkill]
  I --> J[Build Model (Item / Product / Bottle)]
  J --> K[Return normalized instance]
```

Resolvers:

- Own the **order of operations**
- Do not “know” where data comes from
- Delegate lookup/normalization to:
  - StashSkills (how)
  - StashSource (where)

---

## Design Principles

1. **Skills define behavior**  
   Each StashSkill performs one kind of enrichment (UPC, AI, category, etc.).

2. **Resolvers orchestrate**  
   They call skills in a consistent order and then build the final model.

3. **StashSource supplies knowledge**  
   It unifies external APIs, local caches, and ontologies.

4. **Ontologies provide semantic structure**  
   E.g., “Triple Sec ⊂ Orange Liqueur ⊂ Liqueur ⊂ Spirit”.

5. **DataStores persist knowledge**  
   Any store implementing a simple key/value or document interface can be plugged in.

6. **Domain-specific data lives in the application**  
   Barback ships spirits ontology, brand data, and cocktail-centric rules.
