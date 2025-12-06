
# Configuration Examples

## 1. Minimal Config
```
stashkit:
  logging:
    level: WARNING
```

## 2. Enable AI Vision Skill
```
skills:
  ai_vision:
    enabled: true
    provider: openai
    model: gpt-vision-latest
```

## 3. Advanced Resolver Order
```
resolvers:
  product_resolver:
    order:
      - vision_skill
      - taxonomy_skill
      - manual_entry
    conflict_policy: confidence_weighted
```

## 4. Barback Application Config
```
pipelines:
  bottle_pipeline:
    resolvers:
      - bottle_resolver
    persistence:
      write_to_stash: true

stashes:
  bottle_stash:
    backend: sqlite
    path: ./barback_data/bottles.db
```
