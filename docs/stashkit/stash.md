# StashKit Stash

The `Stash` class provides a simple, typed in-memory container for Items or Products.

## Features
- Type-safe
- Iterable
- Mutable
- Queryable using predicates
- Compatible with datastores

## Example
```python
stash = Stash[Product]()
stash.add(Product(name="Example", upc="12345"))
matches = stash.filter(lambda p: p.brand == "Maker's Mark")
```
