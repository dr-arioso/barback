
# Persistence Schema

Every persisted Stash must include:

```
{
  "version": 1,
  "model_type": "Bottle",
  "items": [
      { ... serialized model ... }
  ],
  "indexes": {
      "primary": "...",
      "secondary": { ... }
  },
  "provenance": {
      "created": "...",
      "updated": "..."
  }
}
```

Variations:
- JSON backend stores this structure verbatim
- SQLite backend maps it to relational tables
- HTTP backend may wrap items in API envelopes
