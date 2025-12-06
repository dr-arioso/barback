
# Configuration Layers

StashKit loads configuration in multiple tiers:

1. **Global Defaults**
   - Provided by StashKit core
   - Defines baseline behavior for all modules

2. **StashPack Defaults**
   - Provided by domain packs (e.g., BoozeDexPack, BarbackPack)
   - Adds domain‑specific defaults for Skills, Resolvers, Pipelines

3. **Project-Level Config**
   - Stored in your application's config directory
   - Overrides StashKit and StashPack defaults

4. **Runtime Overrides**
   - Passed programmatically
   - Highest precedence

This layered model allows maximum extensibility while preserving predictable behavior.
