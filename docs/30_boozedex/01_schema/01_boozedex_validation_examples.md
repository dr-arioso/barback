
# BoozeDex Validation Examples

### Valid Example  
```
{
  "brand": "Cointreau",
  "product_name": "Cointreau",
  "classification": "spirits.liqueurs.orange.triple_sec",
  "abv_percent": 40,
  "labeled_volume_ml": 750,
  "country_of_origin": "France"
}
```

### Invalid Example (bad ABV)  
```
{
  "brand": "Lagunitas IPA",
  "product_name": "IPA",
  "classification": "beer.ale.ipa",
  "abv_percent": 35,   # too high for beer
  "labeled_volume_ml": 355
}
```

### Invalid Example (missing classification)  
```
{
  "brand": "Maker's Mark",
  "product_name": "Bourbon",
  "abv_percent": 45,
  "labeled_volume_ml": 750
}
```

These examples support debugging and unit test creation.
