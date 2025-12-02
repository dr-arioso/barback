# Barback Documentation Overview

This document provides a high-level guide to the Barback project and its embedded StashKit library.

## Structure

- **Barback/** — Documents specific to the home-bar project.
  - `architecture.md` — Barback architecture, CLI/TUI/GUI, and home-bar–specific Stashes.
- **StashKit/** — Documents covering the embedded StashKit library in `barback/src/stashkit/`.
  - `API-Overview.md` — StashKit API abstractions and integration points.
  - `Models.md` — Item and Product models.
  - `Resolvers.md` — Resolver module architecture and built-in implementations.
  - `Stash.md` — Generic Stash container.
  - `Output-Plugins.md` — Output plugin specifications.
- **Project Management/** — Planning and reference materials.
  - `roadmap.md` — Development roadmap.
  - `glossary.md` — Definitions of key concepts and terminology.

## Goals

- Clearly separate Barback-specific logic from StashKit library logic.
- Support modular resolvers and output plugins.
- Enable future expansion: HTML reports, multi-output modes, caching, cloud integration.
