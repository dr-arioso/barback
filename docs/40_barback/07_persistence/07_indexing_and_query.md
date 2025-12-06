
# Indexing and Querying

Barback supports:

### Field Queries
- brand
- category (taxonomy path)
- flavor tags
- cocktail roles
- ABV ranges

### Full-Text Search
Against:
- product_name
- brand
- notes
- inferred descriptors

### Tag Queries
```
WHERE tag IN ('bitter', 'aperitif')
```

### SQLite Indexes
Recommended:
- INDEX classification_idx ON bottles(classification)
- INDEX brand_idx ON bottles(brand)
- INDEX abv_idx ON bottles(abv_percent)
