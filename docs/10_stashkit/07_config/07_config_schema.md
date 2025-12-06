
# Configuration Schema

Typical StashKit config file:

```
stashkit:
  logging:
    level: INFO
    timestamp: true

skills:
  upc_skill:
    enabled: true
    api_timeout_ms: 1500

resolvers:
  bottle_resolver:
    order:
      - upc_skill
      - vision_skill
      - ocr_skill
      - manual_entry_skill
    loopback_enabled: true

pipelines:
  bottle_pipeline:
    resolvers:
      - bottle_resolver
    persistence:
      write_to_stash: true

stashes:
  bottle_stash:
    backend: json
    path: ./data/bottles.json
```

All fields can be typed and validated using Pydantic or a similar schema system.
