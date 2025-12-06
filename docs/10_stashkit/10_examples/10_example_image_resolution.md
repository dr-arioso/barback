
# Example: Image-Based Resolution with Skills

This example demonstrates a typical photo-based workflow.

```
from stashkit.skills import UPCSkill, VisionSkill, OCRSkill
from stashkit.resolvers import BottleResolver
from stashkit.pipelines import Pipeline

pipeline = Pipeline(
    resolvers=[BottleResolver()],
    config=Config.load("./config/barback.yaml")
)

result = pipeline.run("./images/bottle.jpg")

print(result.model.product_name)
print(result.model.classification)
print(result.model.abv_percent)
```

This uses:
- UPC detection
- UPC lookup
- AI vision
- OCR fallback
