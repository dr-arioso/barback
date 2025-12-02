# Barback Architecture

## Overview

Barback is a home-bar management project built on top of **StashKit**. It provides:

- User-facing interfaces (CLI, TUI, GUI)
- Home-bar–specific subclasses of StashKit Items, called **Stashes**
- Bar-centric logic for managing, resolving, and outputting home-bar product data

Barback delegates generic product recognition and output tasks to StashKit.

## User Interfaces

Barback provides multiple user-facing interfaces, all of which leverage the underlying StashKit library:

- **CLI** (`barback.py`) — batch-processing entry point
- **Interactive CLI (TUI)** — for interactive inventory management
- **GUI** — planned graphical interface for home-bar management

These interfaces are implemented in Barback, not in StashKit. They all call into StashKit for core processing, resolution, and output generation.

## Major Components

### 1. CLI Layer
- Parses command-line arguments
- Loads configuration
- Selects resolvers & output formats
- Runs home-bar workflows

### 2. Home-Bar Item Management
- Implements Barback-specific `Stash` subclasses
- Aggregates and normalizes home-bar inventory

### 3. Data Flow
1. User Input (CLI/TUI/GUI) →  
2. Barback Stashes →  
3. Resolvers via StashKit →  
4. Merge / Normalize →  
5. Output Plugins →  
6. Artifacts Folder

HTML output optionally embeds:
- Image thumbnails
- Confidence breakdowns
- Resolver comparison tables
