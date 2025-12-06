
# Template: Taxonomy (DexTree) Definition

A minimal taxonomy file:

```
id: boozedex
version: 1.0
type: taxonomy

tree:
  spirits:
    whiskey:
      bourbon:
      rye:
    gin:
    vodka:
  wine:
    red:
    white:
    sparkling:
  beer:
    lager:
    ale:
```

Guidelines:
- Use lowercase, snake_case or dot-separated paths.
- Keep indentation consistent.
- Avoid cycles—builder will validate.
