
# Integrating BoozeDex into Barback

Barback loads BoozeDex during startup:

1. Discover DexPack: `boozedex/`
2. Load compiled taxonomy
3. Load StashTags overlays
4. Register aliases (optional)
5. Provide BoozeDex context to all Resolvers & Skills

Resolvers rely on BoozeDex for:
- taxonomy path resolution
- tag inference
- schema validation
