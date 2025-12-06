
# Booster Pack Structure

A typical Booster Pack has:

```
booster_packs/
  └── boozedex/
        booster.yaml
        dex/
           spirits.yaml
           wine.yaml
           beer.yaml
           liqueurs.yaml
           mixers.yaml
        tags/
           cocktail_roles.yaml
           flavor_profiles.yaml
           usage_roles.yaml
        skills/
           upc.yaml
           vision.yaml
           classification.yaml
        resolvers/
           bottle_resolver.yaml
        pipelines/
           bottle_pipeline.yaml
        templates/
           sqlite_schema.sql
           json_schema.json
        runtime/
           loader.py
           compiler.py
```

Everything inside a Booster Pack is optional but strongly recommended.
