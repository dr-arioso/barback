
# Configuration API

Configuration is accessed via a centralized loader:

```
from stashkit.config import Config

config = Config.load()

timeout = config.skills.upc_skill.api_timeout_ms
resolver_order = config.resolvers.bottle_resolver.order
```

The loader provides:

- layer merging
- validation
- type hints
- environment variable substitution
- optional hot‑reload
