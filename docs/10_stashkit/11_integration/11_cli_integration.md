
# Integration with CLI Applications

StashKit is fully CLI-friendly. Typical patterns:

## Basic CLI workflow

```
from stashkit.pipelines import Pipeline
from stashkit.resolvers import ProductResolver

pipeline = Pipeline(resolvers=[ProductResolver()])

model = pipeline.run("Cointreau").model
print(model.json(indent=2))
```

## Batch processing

```
for path in image_dir.glob("*.jpg"):
    result = pipeline.run(str(path))
    stash.add(result.model)
stash.save()
```

## Interactive prompts (manual entry fallback)

```
if result.warnings:
    print("Missing fields—launching manual entry flow")
```

StashKit avoids any dependency on TTY/terminal features and works cleanly with argparse, click, Typer, and Fire.
