
# Model Design Principles

## 1. Typed Fields
All models must define:
- basic scalar fields (str, int, float)
- structured fields (lists, dicts)
- optional taxonomy path fields

## 2. Validation
Models must enforce:
- required fields
- allowed ranges (e.g., ABV between 0 and 100)
- valid taxonomy references
- conditional validation (e.g., tequila must be agave-based)

## 3. Serialization
Models must support:
- `.dict()`
- `.json()`
- provenance embedding (optional)

## 4. Extensibility
Domain packs (StashPacks) may extend or override models.
