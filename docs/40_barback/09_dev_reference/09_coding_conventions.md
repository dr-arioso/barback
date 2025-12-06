
# Coding Conventions

## Python Style
- PEP8-compliant
- type-annotated
- minimal subclasses unless behavior changes
- explicit imports (no star imports)

## File Layout
```
barback/
  skills/
  resolvers/
  pipelines/
  classification/
  backends/
```

## Docstring Standards
Use Google-style docstrings with examples.

## Error Handling
- Use BarbackError subclasses
- Never raise bare Exception
- Include actionable messages for users
