
# Taxonomy Helpers

Shared helper utilities for interacting with DexNodes and StashDex.

Includes:
- resolving taxonomy paths
- validating paths
- normalizing identifiers
- computing ancestors and descendants
- mapping tags to DexNodes

Example:

```
from stashkit.helpers.taxonomy import resolve_path

node = resolve_path("spirits.whiskey.bourbon")
```

These helpers ensure domain packs can remain consistent without duplicating logic.
