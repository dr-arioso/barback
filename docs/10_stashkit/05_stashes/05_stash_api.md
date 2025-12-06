
# Stash API

```
stash = BottleStash()

stash.add(model)
stash.get(id)
stash.find(upc="...")      # indexed lookup
stash.find_by_taxon(path)  # taxonomy lookup
stash.update(id, model)
stash.delete(id)

stash.export_json()
stash.save()
stash.load()
```

Backends may override:
- `save()`
- `load()`
- `export_*()`
