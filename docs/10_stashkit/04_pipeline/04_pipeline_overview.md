
# Pipeline Subsystem Overview

Pipelines in StashKit provide a structured mechanism for orchestrating a sequence
of resolvers, transformations, validations, and post-processing steps. They act
as the “macro-level” controller above resolvers, coordinating the entire
resolution workflow for a domain task.

A pipeline may:
- prepare inputs (e.g., normalize images, strip whitespace)
- select appropriate resolvers
- coordinate multi-pass resolution
- accumulate provenance across resolvers
- finalize domain objects into stashes
