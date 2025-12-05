# StashKit Models

StashKit defines two primary Pydantic models:

## Item
A generic container for non-product objects:
```python
class Item(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    metadata: dict[str, Any] = Field(default_factory=dict)
```

## Product
Extends `Item` for commercially identifiable products:
```python
class Product(Item):
    upc: Optional[str] = None
    brand: Optional[str] = None
    manufacturer: Optional[str] = None
    volume_ml: Optional[int] = None
```

Applications extend `Product` to represent domain-specific models such as `Bottle`, `Figurine`, `CosmeticProduct`, etc.

Validation occurs only when constructing the final product model, not during resolution.

