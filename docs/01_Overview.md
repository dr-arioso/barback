# Overview

StashKit is a modular framework for turning messy, human-provided input into structured, domain-aware entities. 
It accomplishes this through a coordinated ecosystem of Resolvers, Skills, and StashDexes, with persistent user 
storage handled by the Stash subsystem.

StashKit 1.3 introduces a clarified architecture:
- **StashKit Core**: the orchestrator.
- **Resolvers**: interpret requests by running skill chains.
- **Skills**: small, reusable processors that extract or normalize information.
- **StashDex**: the lexical and ontological reference for a domain.
- **Stash**: the persistent store for resolved entities.
- **BoosterPacks**: pluggable extension bundles containing Dexes, skills, resolvers, and helpers.

This document suite guides you from beginner usage to internal architecture.
