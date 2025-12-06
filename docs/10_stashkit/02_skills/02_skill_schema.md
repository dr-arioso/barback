
# Skill Output Schema

Each Skill returns a dictionary:

```
{
  "result": <any>,
  "confidence": <float>,
  "metadata": {
    "source": "api | ml | regex | rule",
    "latency_ms": <int>,
    "warnings": [<string>],
    ...
  }
}
```

Required:
- `result`
- `confidence`

Optional:
- `metadata`
