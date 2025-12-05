# Project Overview

This project consists of two major components: **StashKit** (a domain-neutral item identification and collection framework with pluggable Item resolution methods and Datastore objects to help with itentification) and **Barback** (a domain-specific extension for managing home bar inventories). StashKit provides generic tools for identifying, enriching, storing, and querying information about products across many domains, while Barback uses these tools to resolve, model, and manage home bars. Initial implementation is limited to Bottles (of spirits, liqueurs, syrups, etc.).

The StashKit system is built around:
- **Items**: generic objects, which may be assigned to a flexible hierarchy
- **Products**: commercially identifiable items with attributes like name, brand, manufacturer, and possibly UPC
- **Resolvers**: orchestrators that combine multiple knowledge providers
- **Skills (Knowledge Providers)**: individual sources of product knowledge (UPC databases, public product catalogs, AI vision, OCR, manual input)
- **Stash**: a typed collection container
- **Datastores**: persistence backends

Example Use Cases:
- A bar manager resolving bottles from UPC scans
- A figurine collector resolving figurines via AI vision
- A hardware inventory system identifying tools via UPC or OCR

