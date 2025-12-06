
# Runtime Loader Examples

## Example 1: BoozeDex Loader

```
def load_pack_runtime(context):
    print("BoozeDex initialized")

    context.aliases.update({
        "bourbon": "spirits.whiskey.bourbon",
        "rye": "spirits.whiskey.rye",
        "gin": "spirits.gin",
    })

    return context
```

## Example 2: IngredientPack Loader

```
def load_pack_runtime(context):
    context.aliases.update({
        "citrus": ["fruit.orange", "fruit.lemon", "fruit.lime"]
    })
    return context
```

## Example 3: Adding Default Tags

```
def load_pack_runtime(context):
    context.tag_registry.add_tag("sweet", applies_to="liqueurs")
    context.tag_registry.add_tag("herbal", applies_to="amari")
    return context
```

Runtime Loaders are intentionally simple and should never perform heavy computation.
