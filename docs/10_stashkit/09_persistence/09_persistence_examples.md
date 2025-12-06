
# Persistence Examples

## 1. JSON Persistence

```
stash = BottleStash(backend="json", path="./bottles.json")
stash.save()    # writes entire stash to file
```

## 2. SQLite Persistence

```
stash = BottleStash(backend="sqlite", path="./bottles.db")
stash.save()
stash.load()    # rehydrates models + indexes
```

## 3. Remote HTTP Persistence

```
stash = BottleStash(backend="http", url="https://api.example.com/stash")
stash.save()
```

## 4. Transient In-Memory Stash

```
stash = BottleStash(backend="memory")
# useful for pipelines that shouldn't persist their output
```
