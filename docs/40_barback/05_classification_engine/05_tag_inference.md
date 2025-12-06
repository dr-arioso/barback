
# StashTag Inference

Tags are inferred automatically based on taxonomy and keywords.

### Rules
- All spirits → base_spirit (unless obviously a modifier)
- Amari → bitter + herbal
- Vermouth → modifier + sweet or dry
- Aperitivo styles → aperitif
- Fruit liqueurs → fruity + sweet + modifier

### Example
Input: "Aperol"
```
{
  "cocktail_roles": ["modifier"],
  "flavor": ["citrus", "bitter"],
  "usage": ["aperitif"],
  "origin": ["italian"]
}
```
