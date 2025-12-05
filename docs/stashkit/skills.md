# Skills (Knowledge Providers)

Skills are small, focused components which answer the question:

> “Given the current partial fields and the raw input, what **additional fields** can I confidently add or refine?”

They do **not** create Pydantic models; they only manipulate dictionaries.

## Skill interface

```python
from typing import Dict, Any, Protocol

class Skill(Protocol):
    def apply(self, fields: Dict[str, Any], input: Dict[str, Any]) -> Dict[str, Any]:
        ...
```

### Example: UPCSkill

```python
class UPCSkill:
    def __init__(self, client):
        self.client = client  # e.g., a UPC DB client

    def apply(self, fields: Dict[str, Any], input: Dict[str, Any]) -> Dict[str, Any]:
        upc = input.get("upc")
        if not upc:
            return fields

        data = self.client.lookup(upc)
        if not data:
            return fields

        # Merge in what we know
        fields.setdefault("upc", upc)
        fields.setdefault("brand", data.get("brand"))
        fields.setdefault("manufacturer", data.get("manufacturer"))
        fields.setdefault("name", data.get("name"))
        return fields
```

### Example: AIVisionSkill

```python
class AIVisionSkill:
    def __init__(self, vision_client):
        self.vision_client = vision_client

    def apply(self, fields: Dict[str, Any], input: Dict[str, Any]) -> Dict[str, Any]:
        image_path = input.get("image_path")
        if not image_path:
            return fields

        guess = self.vision_client.classify(image_path)
        if not guess:
            return fields

        # Only fill if missing
        fields.setdefault("name", guess.get("name"))
        fields.setdefault("category", guess.get("category"))
        return fields
```

### Example: ManualSkill (using a ManualResolver)

```python
class ManualSkill:
    def __init__(self, manual_resolver):
        self.manual_resolver = manual_resolver

    def apply(self, fields: Dict[str, Any], input: Dict[str, Any]) -> Dict[str, Any]:
        return self.manual_resolver.fill_missing(fields)
```

## Application-specific skills

Applications (e.g. Barback or a figurine collector app) can define custom skills which:

- Talk to specialized APIs.
- Apply domain-specific heuristics.
- Enforce domain-specific rules.
