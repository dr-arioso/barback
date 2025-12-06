
# Resolvers Integration

Resolvers direct the flow of classification work.

Barback includes:
- `BottleResolver`
- `WineResolver`
- `BeerResolver`
- (optional future) `RecipeResolver`

Resolvers interact with BoozeDex by:
- mapping features to taxonomy paths
- requesting StashTag inference
- scoring partial results
- performing loopback classification when new data appears
