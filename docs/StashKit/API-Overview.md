# StashKit API Overview

StashKit is a generic library embedded in Barback at `barback/src/stashkit/`. It provides reusable components for:

- Resolvers
- Output plugins
- Item/Stash processing
- Logging and performance tracking

## Architectural Goals
- Decouple library logic from Barback-specific workflows.
- Allow new resolvers or output formats with zero changes to Barback.
- Provide stable, documented interfaces for potential extraction into a standalone repository.
- Support synchronous and asynchronous APIs.

## Features
- Resolver orchestration
- Item aggregation and normalization
- Multi-output support (JSON, CSV, future HTML)
- Logging, caching, and performance metrics
