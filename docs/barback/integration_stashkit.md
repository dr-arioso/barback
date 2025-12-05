# Barback Integration with StashKit

Barback is an **application** that extends StashKit to deal specifically with bottles and bar inventory.

## High-level integration

```mermaid
flowchart LR
    subgraph StashKit
      M[Product model]
      R[ProductResolver]
      SK1[UPCSkill]
      SK2[PublicDBSkill]
      SK3[AIVisionSkill]
      SK4[ManualSkill]
      ST[Stash]
      DS[Datastore]
    end

    subgraph Barback
      B[Bottle model<br/>(extends Product)]
      BR[BottleResolver]
      BK[Barback-specific Skills]
    end

    B --> BR
    BR --> R
    R --> SK1 & SK2 & SK3 & SK4
    R --> M
    M --> ST
    ST --> DS
```

## What Barback imports

From StashKit:

- `Product` (base product model)
- `Stash` (collection)
- `ProductResolver` (base resolver orchestration)
- Skill interfaces and generic skill implementations
- Datastore interfaces

## What Barback defines

- `Bottle` model: `Product` + ABV, category, distiller, dimensions, etc.
- `BottleResolver`: convenience facade around `ProductResolver` configured for bottles.
- Barback-specific skills (if needed), e.g.:
  - A skill that knows about common spirit categories.
  - A skill that consults a local curated bottle database.

Barback **does not** modify StashKit internals; it builds on the public API.
