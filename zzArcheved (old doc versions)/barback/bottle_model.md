# Bottle Model

Extends StashKit Product:

```python
class Bottle(Product):
    abv: Optional[float] = None
    category: Optional[str] = None
    distiller: Optional[str] = None
    height_mm: Optional[float] = None
```

Barback defines properties relevant to spirits, liqueurs, and glass bottles.

