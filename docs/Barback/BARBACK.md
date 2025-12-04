# Barback Documentation

Barback is the spirits-focused inventory application built on StashKit.

It adds:

- A `Bottle` model tailored to spirits and liqueurs
- A `BottleStash` container for inventory
- A `BarbackStashSource` with spirits-specific ontology and brand knowledge
- Concrete resolvers (`BottleResolver`, `GoogleVisionResolver`, `OpenAIVisionResolver`)
- A CLI entrypoint: `barback.py`

---

## 1. Models

### `Bottle` (extends `Product`)

Typical fields:

- `upc: Optional[str]`
- `brand: Optional[str]`
- `manufacturer: Optional[str]`
- `name: Optional[str]` (e.g., "Dry Curacao")
- `abv_percent: Optional[float]`
- `category: Optional[str]` (e.g., "Orange Liqueur", "Curacao", "Triple Sec")
- `distiller: Optional[str]`
- `bottler: Optional[str]`
- `dimensions_cm: Optional[dict[str, float]]` (e.g., height/width)

Barback also uses the ontology to interpret categories in a cocktail-centric way.

### `BottleStash`

`BottleStash` is a `Stash[Bottle]` that provides helpers like:

- `list_brands()`
- `list_categories()`

---

## 2. Spirits Ontology

Barback ships a JSON-based ontology including categories like:

- `Spirit`
  - `Whiskey`
  - `Rum`
  - `Vodka`
  - `Gin`
  - `Liqueur`
    - `Orange Liqueur`
      - `Curacao`
        - `Orange Curacao`
      - `Triple Sec`
    - `Coffee Liqueur`
    - `Amaro`
    - etc.

This enables logic such as:

- “All Curacaos are Orange Liqueurs, but not all Orange Liqueurs are Curacaos.”
- “Blue Curacao is categorized as Orange Liqueur but treated separately for some use cases.”
- Differentiating Triple Sec from Orange Curacao for tiki recipes.

The ontology is **not** hard-coded in StashKit. It lives in the Barback repo under `barback/knowledge/`.

---

## 3. BarbackStashSource

`BarbackStashSource` is a concrete `StashSource` implementation.

Responsibilities:

- Provide metadata based on UPC:
  - Check local DataStores first
  - Query public APIs (e.g., OpenFoodFacts, OpenProductData) as fallbacks
- Normalize brand names via alias maps
- Map noisy textual categories into ontology-backed categories:
  - e.g., "dry curacao", "triple sec", "orange liqueur"
- Merge knowledge from:
  - local JSON data
  - remote APIs
  - user-supplied metadata

Example (conceptual):

```python
source = BarbackStashSource(
    data_stores=[FilesystemStore("./barback_cache"), MemoryStore()],
    ontology=spirits_ontology,
    brand_aliases=brand_alias_table,
)
```

---

## 4. BottleResolver

`BottleResolver` composes multiple StashSkills and a `ProductResolver[Bottle]`:

- `UPCSkill`
- `DBLookupSkill`
- `AIVisionSkill`
- `BrandSkill`
- `CategorySkill`
- `VolumeSkill`
- `DimensionSkill`
- `KeyboardEntrySkill`

A simplified class declaration:

```python
class BottleResolver(
    UPCSkill,
    DBLookupSkill,
    AIVisionSkill,
    BrandSkill,
    CategorySkill,
    VolumeSkill,
    DimensionSkill,
    ProductResolver[Bottle],
):
    ...
```

The concrete implementation:

- Delegates metadata lookups to `BarbackStashSource`
- Uses the ontology to normalize categories
- Uses brand aliases for canonical naming
- Optionally uses OCR or AI models to infer label text from images

---

## 5. Extended AI Resolvers

### `GoogleVisionResolver`

Extends `BottleResolver`, overrides the `AIVisionSkill` behavior to use Google Vision for OCR/label detection.

### `OpenAIVisionResolver`

Extends `BottleResolver`, overrides `AIVisionSkill` to use OpenAI Vision-style models for label reading and structured extraction.

Both preserve the same overall pipeline:

1. UPC (if available)
2. DB lookup (via `BarbackStashSource`)
3. AI Vision
4. Manual completion
5. Model construction

---

## 6. CLI Usage

A conceptual `barback.py`:

```bash
barback --folder ./bottle_photos --resolver bottle
barback --folder ./bottle_photos --resolver google
barback --folder ./bottle_photos --resolver openai
```

Options:

- `--folder`: folder of bottle images
- `--resolver`: which resolver implementation to use (`bottle`, `google`, or `openai`)
- `--no-manual`: disable manual entry step
