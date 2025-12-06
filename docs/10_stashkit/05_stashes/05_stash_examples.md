
# Stash Examples

## 1. BottleStash (Barback)
Indexed by:
- UPC
- taxonomy path (e.g., spirits.whiskey.bourbon)
- normalized name
- brand

Example:
```
stash.add(bottle_model)
result = stash.find(upc="012345678905")
```

## 2. ProductStash
Generic stash for taxon-linked objects.

## 3. MetadataStash
Stores enriched metadata from multi-resolver pipelines.

## 4. SessionStash
Temporary in-memory stash for ephemeral pipeline runs.
