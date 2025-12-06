
# Taxonomy Integration with Models

All models may include:

- `classification` (canonical taxonomy path)
- `taxon` (DexNode reference)
- `tags` (derived from StashTags)
- `roles` (cocktail or usage roles)
- `ancestors` (taxonomy lineage for indexing)

Resolvers attach this automatically after classification.

Stashes index models using these taxonomy fields.
