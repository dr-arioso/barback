
# StashKit Core Architecture Overview

StashKit is a modular data orchestration framework designed around four pillars:
1. **StashDex** – taxonomy and metadata engine.
2. **Skills** – atomic inference and extraction units.
3. **Resolvers** – orchestration logic coordinating skills and conflict resolution.
4. **Stashes** – persistent indexed collections of structured domain objects.

The core provides lifecycle, configuration, loading, error handling, caching, runtime utilities, and BoosterPack integration.
