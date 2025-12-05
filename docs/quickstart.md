# Quickstart

This guide walks through a minimal end-to-end example using **StashKit** and **Barback**.

## 1. Install & layout

Your repo is structured roughly as:

```text
src/
  stashkit/
  barback/
docs/
```

Make sure StashKit is importable (editable install or `PYTHONPATH`).

## 2. Create a simple Product and Stash

```python
from stashkit.models import Product
from stashkit.stash import Stash

stash = Stash[Product]()
p = Product(name="Example Bottle", upc="0123456789")
stash.add(p)
```

## 3. Define a simple UPC skill

```python
from typing import Dict, Any

class DummyUPCSkill:
    def apply(self, fields: Dict[str, Any], input: Dict[str, Any]) -> Dict[str, Any]:
        if "upc" in input and input["upc"] == "0123456789":
            fields.setdefault("brand", "Demo Brand")
            fields.setdefault("manufacturer", "Demo Distillery")
        return fields
```

## 4. Use a ProductResolver

```python
from stashkit.resolvers import ProductResolver
from stashkit.models import Product

resolver = ProductResolver(
    model=Product,
    skills=[DummyUPCSkill()],
)

product = resolver.resolve({"upc": "0123456789"})
stash.add(product)
```

## 5. Extend to Barback's Bottle

```python
from barback.models import Bottle
from barback.resolvers import BottleResolver

bottle_resolver = BottleResolver(
    model=Bottle,
    skills=[DummyUPCSkill(), ...],  # add vision, public DB, manual skills as you implement them
)

bottle = bottle_resolver.resolve({"upc": "0123456789"})
```

From here, you can persist the `stash` via a Datastore, or feed bottles into a shelf-layout tool.
