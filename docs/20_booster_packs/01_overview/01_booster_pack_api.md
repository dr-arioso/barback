
# Booster Pack API

## Activate a pack

```
from stashkit import activate_pack
activate_pack("boozedex")
```

## Query active pack

```
from stashkit import current_pack
print(current_pack())
```

## Load pack programmatically

```
from stashkit.booster_packs import load_pack
pack = load_pack("./custom_pack")
```

## Pack Metadata

Each pack defines:

```
name: "boozedex"
version: "1.0"
description: "Beverage taxonomy + metadata"
dependencies:
  - stashkit>=1.0
```

Booster Packs behave somewhat like Python packages, but with structured data rather than code.
