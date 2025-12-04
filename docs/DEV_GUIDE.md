# Developer Guide

This guide explains how to set up a development environment, navigate the code, and extend Barback and StashKit.

---

## 1. Repository Layout

Conceptual layout:

```text
.
├─ src/
│   └─ stashkit/
│       ├─ models/
│       ├─ stash/
│       ├─ resolvers/
│       │   └─ skills/
│       └─ sources/
└─ barback/
    ├─ models.py
    ├─ inventory/
    ├─ knowledge/
    ├─ resolvers/
    ├─ core/
    └─ barback.py
```

---

## 2. Getting Started

1. Create and activate a virtual environment.
2. Install dependencies (example):
   ```bash
   pip install pydantic requests
   # optionally: google-cloud-vision, openai, pytesseract, etc.
   ```
3. Add `src/` to your `PYTHONPATH` or install `stashkit` as an editable package:
   ```bash
   pip install -e ./src
   ```

---

## 3. Implementing StashKit Core (From Scratch)

Follow this order:

1. **Models**
   - Implement `Item` and `Product` using Pydantic.
2. **Stash**
   - Implement a generic `Stash[T]` container with `add()` and iteration.
3. **Resolvers**
   - Implement `ResolutionContext` (upc, image_path, fields).
   - Implement `BaseResolver[T]` with the pipeline described in `STASHKIT.md`.
   - Implement `ItemResolver` and `ProductResolver` as thin specializations.
4. **StashSource**
   - Define the abstract `StashSource` interface.
   - Implement `InMemoryStashSource` for local experiments.
5. **DataStores**
   - Implement `MemoryStore` and `FilesystemStore`.
6. **Ontology**
   - Implement an ontology that can:
     - Add nodes and edges
     - Return ancestors/descendants
     - Deal with aliases
7. **StashSkills**
   - Implement skills one at a time:
     - `UPCSkill`, `DBLookupSkill`, `AIVisionSkill`, `BrandSkill`, `CategorySkill`, `VolumeSkill`, `DimensionSkill`, `KeyboardEntrySkill`.

Use `EXAMPLES.md` as a reference for signatures and patterns.

---

## 4. Implementing Barback (From Scratch)

1. **Bottle Model**
   - Define `Bottle(Product)` in `barback/models.py`.
2. **BottleStash**
   - Implement `BottleStash(Stash[Bottle])` with helper methods.
3. **Spirits Ontology**
   - Create JSON ontology under `barback/knowledge/spirits_ontology.json`.
4. **Brand Aliases**
   - Store brand data under `barback/knowledge/brands.json`.
5. **BarbackStashSource**
   - Implement `BarbackStashSource(StashSource)`:
     - Uses File/Memory DataStores
     - Loads ontology & brand aliases
     - Implements `lookup`, `normalize_brand`, `normalize_category`.
6. **BottleResolver**
   - Compose skills and `ProductResolver[Bottle]` as shown in `BARBACK.md`.
7. **Pipeline**
   - Implement `run_pipeline(...)` in `barback/core/pipeline.py`.
8. **CLI**
   - Implement `barback.py` which:
     - Parses command line args
     - Instantiates `BarbackStashSource` and chosen resolver
     - Calls `run_pipeline`
     - Outputs a summary of the BottleStash.

---

## 5. Adding a New Domain Example: Fruit

1. Create `Fruit(Item)` in a new `fruit` app.
2. Create `FruitStash(Stash[Fruit])`.
3. Implement a `FruitOntology` for classification.
4. Implement `FruitStashSource`.
5. Implement `FruitResolver(AIVisionSkill, CategorySkill, KeyboardEntrySkill, ItemResolver[Fruit])`.
6. Write a small CLI or script to process fruit images.

---

## 6. Testing Strategy

- Unit tests for:
  - Each StashSkill (in isolation)
  - Each StashSource method (with API mocks)
  - Ontology operations
  - Resolver pipelines (with mocked StashSource)
- Integration tests for:
  - Complete Barback pipeline from image folder to BottleStash
