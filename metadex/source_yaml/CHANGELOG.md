# MetaDex Changelog

## [1.3.0] — 2025-12-07

### Added

- **Stash** subsystem:
  - Models persistent user collections of resolved entities.
  - Introduces a `dex_table` for mapping short keys (e.g. `D1`) to fully-qualified Dex identifiers
    (e.g. `BoozeDex.2025.04`).
  - Defines APIs for `add`, `get`, `list`, `update`, and optional `re_resolve`.

- Expanded **StashDex** semantics:
  - Clarified as a lexical + ontological reference, not the user storage layer.
  - Added `alias_maps`, `classification_axes` fields.
  - Added `resolve_alias` and `infer` public methods.

- Expanded **Resolver** semantics:
  - Added fields such as `target_entity_type`, `required_fields`, `optional_fields`,
    `skill_sequence`, `termination_rules`, `conflict_resolution_strategy`, `supported_dexes`.
  - Clarified resolvers as orchestrators of skill sequences that produce entities
    suitable for persistence in Stashes.

- Expanded **Skill** semantics:
  - Added `signal_type`, `produces_fields`, `domain_specific`, `requires_context`.
  - Clarified skills as producers of field-level proposals, often with confidence
    and provenance information.

- Clarified **BoosterPacks**:
  - BoosterPacks may include Dexes, entity schemas, resolvers, skills, and helper utilities.

- New rules:
  - Consistency between resolver-supported Dexes and stash Dex references.
  - Structural rule ensuring stash entities reference Dexes through the `dex_table`.

### Changed

- Removed `barback.core` from MetaDex (Barback is treated as an application built on StashKit).
- Clarified that StashDex is not the storage layer; Stash is.

### Removed

- `barback.core` entity and related relationships.
