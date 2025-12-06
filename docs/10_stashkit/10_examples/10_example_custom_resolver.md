
# Example: Custom Resolver

```
from stashkit.resolvers import BaseResolver

class MyResolver(BaseResolver):
    order = ["vision_skill", "custom_skill"]

    def consolidate(self, results):
        # Custom merging logic
        return super().consolidate(results)
```

Register via config:

```
resolvers:
  my_resolver:
    order:
      - vision_skill
      - region_skill
```
