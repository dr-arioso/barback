
# Build Pipeline API

Basic usage:

```
from stashkit.booster_packs import build_pack

result = build_pack("./booster_packs/boozedex")
print(result.artifacts)
```

Build API returns an object:

```
{
  "manifest": {...},
  "compiled_taxonomies": {...},
  "compiled_tags": {...},
  "merged_config": {...},
  "debug": {...}
}
```

Advanced usage:

```
build_pack(path, strict=True, output_format="json")
```

Options:
- `strict` — fail on any warning  
- `output_format` — json, msgpack, yaml  
