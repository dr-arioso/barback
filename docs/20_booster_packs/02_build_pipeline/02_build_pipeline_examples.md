
# Build Pipeline Examples

## Building BoozeDex

```
build_pack("./booster_packs/boozedex")
```

Output includes:
- `boozedex_taxonomy.json`
- `boozedex_tags.json`
- `boozedex_config.json`
- `manifest.json`
- debug lineage maps

## Custom Build Pipeline Rules

A Booster Pack can define a custom build phase:

```
build:
  phases:
    - validate_labels
    - compile_taxonomy
    - enrich_with_gs1
```

StashKit will import and run these phases automatically.
