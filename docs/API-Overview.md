# Barback / StashKit – API Overview

This document summarizes the planned architecture as Barback evolves toward a more modular system centered around **StashKit**, a pluggable framework for:
- **Image ingestion**
- **Resolver backends** (OpenAI Vision, Google Vision, barcode-only, cached results, etc.)
- **Output plugins** (JSON, CSV, future HTML)
- **Shared utility layers** (logging, path resolution, product-metadata formatting)

Barback will continue to be the CLI/GUI wrapper.  
StashKit will hold the reusable logic.

## Architectural Goals
- Cleanly separate **core logic** from the Barback application layer.
- Allow new resolvers or output formats with **zero changes** to Barback.
- Provide a stable, documented interface before extracting StashKit into its own repository.
- Offer both synchronous and asynchronous APIs.
