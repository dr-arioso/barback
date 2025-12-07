# MetaDex

MetaDex is the canonical, machine-readable ontology for **StashKit**.

It defines:

- Core system and subsystems (StashKit Core, Resolvers, Skills, StashDex, Stash, BoosterPacks)
- Their responsibilities, traits, and public APIs
- Relationships between components (uses, consults, may_include, references)
- Structural and consistency rules used by tooling

MetaDex is authored as YAML in `source_yaml/` and compiled to a single JSON artifact
in `metadex/metadex.json` by the provided compiler.

## Versioning

Current MetaDex schema version: **1.3.0**

See `CHANGELOG.md` for what changed relative to 1.2.x.
