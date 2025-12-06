
# Resolver Output Schema

Resolvers produce a dictionary:

```
{
  "model": <DomainModel>,
  "confidence": <float>,      # summary confidence
  "fields": { ... },           # per-field confidence + provenance
  "provenance": [ ... ],       # skill-by-skill log
  "warnings": [ ... ],
  "conflicts": [ ... ]
}
```

The `model` is always a fully validated Pydantic or dataclass object.
