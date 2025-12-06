
# Persistence Backends

The following storage backends are supported or planned:

## 1. JSON Backend (default)
- Human-readable
- Easy to diff and version-control
- Low performance overhead for small–medium datasets

## 2. SQLite Backend
- More scalable
- ACID-compliant
- Allows indexed queries
- Recommended for applications with larger inventories (e.g., bars with >500 bottles)

## 3. Remote HTTP Backend
- Enables multi-device sync
- Works well with mobile apps or cloud-hosted dashboards
- Allows domain packs to offer hosted metadata (e.g., BoozeDex API)

## 4. Memory Backend
- Used for ephemeral pipeline runs
- Does not persist after application exit

Each backend adheres to the same interface, ensuring that Stashes can swap backends without behavioral changes.
