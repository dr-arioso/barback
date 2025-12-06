
# Stashes Subsystem Overview

A **Stash** is StashKit’s structured, indexed, persistence-friendly container
for domain objects. Stashes allow pipelines and resolvers to store fully-resolved
domain models using consistent APIs across all domains (Barback, BoozeDex, or
custom apps).

Stashes behave like a hybrid of:

- A typed collection
- An indexable lightweight database
- A persistence façade
- A provenance-aware storage layer

They enforce validation, indexing, and reliable long-term retrieval of
structured objects.
