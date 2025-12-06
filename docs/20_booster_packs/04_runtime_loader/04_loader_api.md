
# Runtime Loader API

A Booster Pack may expose a loader:

```
def load_pack_runtime(context):
    # Perform runtime initialization
    return context
```

StashKit’s loader discovers and executes this function after build artifacts
are loaded.

### Example Integration

```
from stashkit import activate_pack

activate_pack("boozedex")
```

Internally:

1. Discover pack directory  
2. Load build artifacts (compiled taxonomies, tags, config)  
3. Execute loader:  
   ```
   pack.runtime.load_pack_runtime(context)
   ```  
4. Merge into global StashKit registries  

### Context Object

The context passed to runtime loaders provides:

```
context.taxonomy_registry
context.tag_registry
context.skill_registry
context.resolver_registry
context.pipeline_registry
context.config
context.aliases
```

The loader may add or modify entries.
