# StashKit Architecture

StashKit is a **generic product framework**. It knows about Items, Products, Resolvers, Skills, Stashes, and Datastores — but it does **not** know anything about specific domains (alcohol, figurines, hardware, etc.).

## High-level flow

```mermaid
flowchart LR
    A[Raw Input<br/>(UPC, image, text)] --> B[Resolver]
    B --> C1[Skill 1<br/>(UPC DB)]
    B --> C2[Skill 2<br/>(Public DB)]
    B --> C3[Skill 3<br/>(AI Vision)]
    B --> C4[Skill 4<br/>(Manual Input)]

    C1 --> D[Fields dict]
    C2 --> D
    C3 --> D
    C4 --> D

    D --> E[Validated Product Model]
    E --> F[Stash]
    F --> G[Datastore]
```

- **Raw Input**: Provided by the application (UPC codes, file paths, user text, etc.).
- **Resolver**: Orchestrates a list of Skills in an application-defined order.
- **Skills**: Independent knowledge providers that enrich a shared `fields` dict.
- **Product Model**: Pydantic `Product` or subclass (e.g. `Bottle`).
- **Stash**: Container of Items/Products.
- **Datastore**: Persistence layer.

## Component diagram

```mermaid
graph TD
  subgraph StashKit
    M[Item / Product models]
    R[Resolver base]
    S[Skill interface]
    ST[Stash]
    D[Datastore interface]
  end

  subgraph Application (e.g. Barback)
    BM[Bottle model<br/>(extends Product)]
    BR[BottleResolver<br/>(uses ProductResolver)]
    BS[App-specific Skills]
  end

  M --> R
  R --> S
  R --> M
  M --> ST
  ST --> D

  BM --> BR
  BR --> BS
  BR --> M
```

StashKit defines the **interfaces and generic implementations**; applications wire them together with domain-specific models and skills.
