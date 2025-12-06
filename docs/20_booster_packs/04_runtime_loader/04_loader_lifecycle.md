
# Runtime Loader Lifecycle

The Runtime Loader performs the following sequence:

## 1. Initialization
- Receive context from StashKit’s loader (`context`)
- Load manifest produced by the Build Pipeline
- Validate runtime-ready files exist (taxonomy.json, tags.json, config.json)

## 2. Register DexTree
- Attach compiled taxonomy trees to StashKit’s taxonomy registry
- Generate ancestor/descendant caches
- Validate global node uniqueness across packs

## 3. Register StashTags
- Load compiled tag definitions
- Register tag groups and tag → DexNode mappings
- Build inverted indices for fast resolution

## 4. Register Skills / Resolvers / Pipelines
- Map declared names to implementations
- Apply config defaults from Booster Pack
- Validate references to taxonomy or tag paths

## 5. Apply Config Overlays
- Merge Booster Pack–provided config into global config
- Respect precedence rules:
  1. Runtime overrides  
  2. Project-level config  
  3. Booster Pack defaults  
  4. StashKit defaults  

## 6. Alias Registration (Optional)
- Register shorthand category names:
  - `"bourbon"` → `"spirits.whiskey.bourbon"`
  - `"bitters"` → `"liqueurs.bitter.amaro"` (example)
- Used by Resolvers and manual entry flows

## 7. Finalization
- Return updated runtime context
- Loader must be idempotent
- Must not leak global mutable state
