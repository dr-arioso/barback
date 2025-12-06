
# Template: Runtime Loader

Booster Packs can include a custom loader that runs after compilation.

```
def load_pack_runtime(context):
    print("BoozeDex runtime initialized")
    context.register_alias("vodka", "spirits.vodka")
    return context
```

Loaders may perform:
- alias registration  
- name normalization  
- provenance injection  
- custom tag expansions  
