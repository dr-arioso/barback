
# Runtime Loader Overview

The **Runtime Loader** is the execution-time component of a Booster Pack.
While the Build Pipeline compiles human-authored YAML into efficient artifacts,
the Runtime Loader integrates those artifacts into StashKit’s active runtime
environment.

The Loader ensures that a Booster Pack becomes *active*, meaning:

- taxonomy DexTrees are registered  
- StashTags are loaded  
- Skills, Resolvers, and Pipelines are mapped  
- configuration overlays are applied  
- aliases and shorthand names are registered  
- custom runtime hooks execute as needed  

The Loader is lightweight and fast — it must be safe to run many times.
