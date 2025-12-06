
# BoozeDex JSON Schema (Generated)

This represents the machine-validated version of BoozeDex's model definitions.
Booster Packs may include this schema for client-side validation.

```
{
  "title": "BoozeDex Product",
  "type": "object",
  "properties": {
    "brand": { "type": "string" },
    "product_name": { "type": "string" },
    "classification": { "type": "string" },
    "abv_percent": { "type": "number", "minimum": 0, "maximum": 100 },
    "labeled_volume_ml": { "type": "integer", "minimum": 1 },
    "country_of_origin": { "type": ["string", "null"] },
    "aliases": { "type": "array", "items": { "type": "string" } }
  },
  "required": ["brand", "product_name", "classification", "abv_percent", "labeled_volume_ml"]
}
```
