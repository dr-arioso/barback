
# Persistence Examples

## Insert Example
```
backend.insert({
  "brand": "Aperol",
  "product_name": "Aperol",
  "classification": "spirits.liqueurs.herbal.aperitivo.aperol_style",
  "abv_percent": 11,
  "volume_ml": 750,
  "confidence": 0.96
})
```

## Merge Example
Existing:
- ABV: 40% (confidence 0.55)

Incoming:
- ABV: 42% (confidence 0.92)

Result:
```
abv_percent = 42%
confidence = 0.92
```

## Query Example
```
backend.search(tags=["bitter"], abv_min=10, abv_max=40)
```

