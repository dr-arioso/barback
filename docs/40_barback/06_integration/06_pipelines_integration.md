
# Pipelines Integration

The pipeline orchestrates the full resolution flow.

Barback provides:
- `bottle_pipeline`
- `wine_pipeline`
- `beer_pipeline`

Each pipeline:
1. Invokes a resolver sequence
2. Merges all skill outputs
3. Delegates classification to the Classification Engine
4. Updates the stash backend

Pipelines rely on BoozeDex taxonomies to validate classification paths.
