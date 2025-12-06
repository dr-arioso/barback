
# ResolverPack Template

## Overview
A ResolverPack bundles one or more resolvers that orchestrate skill execution.

## Directory Structure
```
resolverpack-example/
  booster.yaml
  resolvers/
    example_resolver.py
```

## booster.yaml
```yaml
name: resolverpack-example
version: 0.1.0
type: resolverpacks
entry_points:
  resolvers: resolvers/
dependencies: []
```

## resolvers/example_resolver.py
```python
from stashkit.resolvers import BaseResolver

class ExampleResolver(BaseResolver):
    name = "example-resolver"

    def resolve(self, input, stash):
        # Use skills, apply logic
        return {"resolved": True}
```

## Notes
- Resolvers coordinate multiple Skills.
