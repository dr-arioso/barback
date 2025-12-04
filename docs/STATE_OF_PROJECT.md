# State of the Project

Barback and StashKit now share a coherent, extensible architecture that supports:

- Structured ingestion of Items and Products
- A pipeline-based resolver model
- Composable behavioral mixins called **StashSkills**
- A pluggable knowledge-provider abstraction: **StashSource**
- Ontology-driven category inference and normalization
- Pluggable DataStores for persistence and caching
- Clear separation of:
  - domain-neutral logic (StashKit), and
  - domain-specific logic (Barback, spirits ontology, etc.)

StashKit is intended to be reusable across many domains: fruit, groceries, tools, cards, miniatures, etc.

Barback is the first opinionated application built on StashKit and focuses on:

- Bottles of spirits and liqueurs
- Cocktail-relevant categorization
- Brand/alias management
- UPC + AI + manual entry pipeline
