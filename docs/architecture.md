# Barback Architecture (Expanded)

## Overview

Barback is a CLI-driven batch-product-recognition pipeline. It processes folders of images and extracts structured data using one or multiple “resolvers.” Output formats include JSON, CSV, and a planned HTML report with inline thumbnails.

Barback will eventually depend on **StashKit**, a reusable library that provides:
- A unified Resolver API
- Output plugins
- A shared Item model
- Consistent error handling
- Logging and performance tracking

## Major Components

### 1. **CLI Layer (barback.main)**
- Reads arguments
- Loads configuration
- Selects resolvers & output formats
- Manages batch execution

### 2. **Resolvers (barback.resolvers.*)**
Example implementations:
- OpenAI Vision
- Google Vision
- Barcode-only extraction
- Local ML models (future)

A resolver must:
- Accept a file path
- Return an Item object with fields: name, brand, barcode, confidence, tags, raw

### 3. **StashKit Core (future)**
Responsible for:
- Resolver orchestration
- Item aggregation
- Future caching
- Future fallback resolution

### 4. **Outputs**
Current:
- JSON
- CSV

Planned:
- HTML with inline thumbnails
- “Multi-output mode” (CSV+HTML+JSON in same run)

### 5. **Data Flow Diagram**

1. Input →  
2. Resolver(s) →  
3. Merge / Normalize →  
4. Output Plugins →  
5. Artifacts Folder

HTML output will optionally embed:
- image thumbnails
- confidence breakdowns
- resolver comparison table
