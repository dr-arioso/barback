
# Persistence Subsystem Overview

The **Persistence subsystem** defines how Stashes and Pipelines store and load
resolved domain models, provenance, and supporting metadata. It provides a
uniform abstraction over multiple backend types while ensuring data integrity,
schema validation, and predictable write/read behavior.

Persistence is intentionally modular—backends can be swapped or extended without
changing the Stash or Pipeline logic.
