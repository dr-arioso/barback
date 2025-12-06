
# Classification Output Format

The final model includes:

```
{
  "classification": "spirits.whiskey.bourbon",
  "tags": {
    "cocktail_roles": ["base_spirit"],
    "flavor": ["woody", "sweet"],
    "origin": ["american"]
  },
  "confidence": 0.91,
  "provenance": {
    "inputs": [...],
    "skills": [...],
    "resolver_trace": [...],
    "alternates": [...],
    "timestamp": "..."
  }
}
```

This output feeds directly into Resolvers and Pipelines.
