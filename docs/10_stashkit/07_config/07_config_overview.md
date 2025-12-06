
# Configuration Subsystem Overview

The **Configuration subsystem** defines how StashKit loads and manages
settings for Skills, Resolvers, Pipelines, Stashes, and Booster Packs.
Configuration is declarative, environment‑aware, and supports strong typing.

StashKit configuration aims to be:

- **Predictable** — no hidden defaults
- **Explicit** — every module describes the config it consumes
- **Composable** — domain packs can extend or override settings
- **Multi‑layered** — supports global, project, and run‑level config

Configuration files are typically YAML for human editing, with optional
pre‑compilation into JSON for runtime speed.
