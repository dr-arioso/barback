
# Barback Persistence Overview

Persistence in Barback ensures bottles, wines, beers, mixers, and metadata are
stored reliably after classification.

Barback relies on StashKit’s Backend system, which offers:

- JSON backend (simple, human-readable)
- SQLite backend (structured, queryable)
- Custom or cloud backends (future expansion)

Barback ships with recommended schema definitions and persistence flows for bottle
inventory use cases.
