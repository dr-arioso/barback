# Resolvers

Resolvers are responsible for taking **raw input** (UPC codes, image paths, text blobs, etc.), passing that input through a sequence of **Skills**, and finally constructing a **validated Pydantic model**.

## Core ideas

- A Resolver is configured with:
  - A target model class (usually `Product` or a subclass).
  - An ordered list of Skills.
- Each Skill receives:
  - The current `fields` dict.
  - The original `input` dict.
- Each Skill returns an updated `fields` dict.
- After all Skills run, the Resolver builds and validates the model:
  `model(**fields)`.

## Example interface

```python
from typing import Dict, Any, List, Protocol, Type
from pydantic import BaseModel

class Skill(Protocol):
    def apply(self, fields: Dict[str, Any], input: Dict[str, Any]) -> Dict[str, Any]:
        ...

class ProductResolver:
    def __init__(self, model: Type[BaseModel], skills: List[Skill]):
        self.model = model
        self.skills = skills

    def resolve(self, input: Dict[str, Any]) -> BaseModel:
        fields: Dict[str, Any] = {}
        for skill in self.skills:
            fields = skill.apply(fields, input)
        return self.model(**fields)
```

## Why Skills return dicts

Each Skill typically knows only **part** of the truth about a product:

- A UPC DB might know brand and name.
- A public DB might know volume and manufacturer.
- Vision may guess category or color.
- Manual entry fills in missing values.

Returning dicts allows these partial contributions to be merged before final validation.
