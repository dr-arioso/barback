
# Standard Model Schema

A model must include:

```
class Bottle(BaseModel):
    id: str
    brand: str
    product_name: str
    classification: str    # taxonomy path
    labeled_volume_ml: int
    abv_percent: float
    metadata: dict = {}
```

Additional optional fields:
- `aliases`
- `tags`
- `sku`
- `origin_country`
- `description`
- `provenance`
