
# Logging Helpers

StashKit includes helper utilities for structured logging.

## Features
- JSON or text log formatting
- skill-level and resolver-level prefixes
- automatic provenance event formatting
- pluggable sinks (stdout, file, rotating logs)

## Example

```
from stashkit.helpers import log

log.info("Resolver started", resolver="bottle_resolver")
log.warning("Low confidence detected", confidence=0.33)
log.error("Skill failed", skill="vision_skill", error="timeout")
```

All logs are designed to be machine readable.
