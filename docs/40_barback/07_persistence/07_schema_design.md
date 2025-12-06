
# Recommended Schema Design

Barback stores the full classified output model.

### Core Fields
```
id: UUID
brand: string
product_name: string
classification: string
abv_percent: float
volume_ml: int
tags: object
```

### Provenance Fields
```
confidence: float
resolver_trace: [...]
skill_outputs: [...]
source_priority: [...]
timestamp: string
```

### Optional Metadata
```
notes: string
image_paths: [...]
location: bar / storage / shelf
```

### SQLite Tables
Recommended tables:
- bottles
- tags
- provenance
- images
