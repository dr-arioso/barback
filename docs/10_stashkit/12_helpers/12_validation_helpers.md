
# Validation Helpers

Used across Skills, Resolvers, Pipelines, and Stashes.

Includes:
- numeric validation (range checks)
- string validation (nonempty, ASCII, unicode-safe)
- model field validators
- schema utilities for optional and required fields

Example:

```
from stashkit.helpers.validate import ensure_range

ensure_range(abv, 0, 100, field="abv_percent")
```
