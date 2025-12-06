
# StashPack Template

## Overview
A StashPack is a full domain pack combining multiple Booster types.

## Directory Structure
```
stashpack-example/
  booster.yaml
  config/
    defaults.yaml
  dependencies/
    boosters.yaml
```

## booster.yaml
```yaml
name: stashpack-example
version: 0.1.0
type: stashpacks
description: "Complete domain pack"
entry_points:
  config: config/
dependencies:
  - dexpacks: mydexpack
  - tagpacks: tagpack-example
  - skillspacks: skillspack-example
  - resolverpacks: resolverpack-example
```

## config/defaults.yaml
```yaml
resolver: example-resolver
skills_enabled:
  - example-skill
```

## dependencies/boosters.yaml
```yaml
required:
  - mydexpack
  - tagpack-example
  - skillspack-example
  - resolverpack-example
```

## Notes
- StashPacks define the full environment for a domain.
