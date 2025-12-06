
# Persistence API

Stashes delegate persistence through a unified API:

```
stash = BottleStash(backend="sqlite", path="./data/bottles.db")

stash.save()    # write everything
stash.load()    # restore previous state

stash.export_json(path)
stash.import_json(path)
```

Backends must provide:

- `save(stash_state)`
- `load() -> stash_state`
- `export_*()`
- `import_*()`

Backends *may* add advanced features (e.g., journaling, batch writes).
