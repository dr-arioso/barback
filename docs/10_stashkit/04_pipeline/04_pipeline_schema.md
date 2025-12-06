
# Pipeline Output Schema

A typical pipeline returns:

```
{
  "model": <DomainModel>,
  "pipeline_confidence": <float>,
  "resolver_outputs": [...],
  "logs": [...],
  "warnings": [...],
  "provenance": [...],
  "stash_write_result": <optional>
}
```

All components must be serializable for debugging and reproducibility.
