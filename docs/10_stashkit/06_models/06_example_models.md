
# Example Models

## 1. Bottle Model (Barback)
```
class Bottle(BaseModel):
    id: str
    brand: str
    product_name: str
    classification: str
    labeled_volume_ml: int
    abv_percent: float
    sku: str | None = None
    metadata: dict = {}
```

## 2. Product Model (Generic)
```
class Product(BaseModel):
    id: str
    name: str
    classification: str
    attributes: dict = {}
```

## 3. Metadata Model
```
class Metadata(BaseModel):
    id: str
    fields: dict
    confidence: float
    provenance: list
```
