
# Conflict Handling in Persistence

Conflicts occur when a bottle already exists in storage.

Strategies:
- **Replace**: overwrite previous entry
- **Merge**: unify fields (default)
- **Append**: treat as new bottle (different SKU or volume)

Merge logic:
- Prefer higher-confidence fields
- Prefer newer data (by timestamp)
- Maintain provenance history

Users may optionally verify merges in UI/CLI.
