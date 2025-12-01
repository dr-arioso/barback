# StashKit API (Draft)

## Purpose

StashKit abstracts away:
- Resolvers
- Output plugins
- Item models
- Logging
- Future distributed compute

## Item Object (Core Model)

```python
class Item:
    id: str
    name: str | None
    brand: str | None
    barcode: str | None
    confidence: float | None
    tags: list[str]
    raw: dict
    source_path: str
```

## Resolver Interface

```python
class BaseResolver:
    def resolve(self, image_path: str) -> Item | None:
        raise NotImplementedError
```

## Output Plugin Interface

```python
class BaseOutput:
    def write(self, items: list[Item], output_dir: str) -> None:
        ...
```

Planned outputs:
- JSON
- CSV
- HTML
- SQLite
