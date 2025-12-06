
# Storage Backends

Barback supports multiple backend types:

## JSONBackend
- Best for small personal inventories
- Human-editable
- Version-control-friendly

## SQLiteBackend
- Fast queries
- Ideal for mobile + desktop apps
- ACID-compliant
- Handles large inventories

## Custom Backend (Optional)
Developers may supply:
- REST API backend
- Encrypted local backend
- Cloud-synced backend

Barback's persistence layer is backend-agnostic.
