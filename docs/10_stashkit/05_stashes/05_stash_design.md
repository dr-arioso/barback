
# Stash Design Principles

## 1. Typed Storage
Each stash stores one model type:
- BottleStash → Bottle models
- ProductStash → generic Product models
- MetadataStash → metadata bundles

## 2. Index-Enriched
Stashes may maintain:
- primary index (ID)
- secondary indexes (UPCs, names)
- taxonomy indexes (from DexNodes)
- alias indexes
- timestamp indexes

## 3. Persistence-Agnostic
The stash API does not depend on how data is stored.
Backends are pluggable.

## 4. Provenance-First
Every item records:
- resolver chain
- skill outputs
- pipeline info
- creation/update time

## 5. Safety & Validation
All writes require:
- model validation
- duplicate detection (optional)
- conflict handling
