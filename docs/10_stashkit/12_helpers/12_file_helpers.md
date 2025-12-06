
# File and Path Helpers

Thin wrappers over filesystem operations to ensure consistent behavior across
platforms and backends.

Includes:
- safe path joining
- temp file creation
- JSON / YAML loader wrappers
- path normalization for Windows/macOS/Linux

Example:

```
from stashkit.helpers.files import load_yaml

config = load_yaml("./config/stashkit.yaml")
```
