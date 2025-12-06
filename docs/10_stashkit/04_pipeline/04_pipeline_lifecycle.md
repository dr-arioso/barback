
# Pipeline Lifecycle

1. **Initialization**
   - Pipeline loads configuration (resolver order, error policy, output targets).
   - Pipeline selects the domain StashPack if one is active (e.g., Barback).

2. **Preprocessing Stage**
   - Normalize inputs
   - Convert file formats
   - Extract metadata (timestamp, filename, EXIF)

3. **Resolver Execution Stage**
   - Pipeline iterates through resolvers in configured order.
   - Each resolver receives the current working state.
   - Early termination is allowed if sufficient confidence is reached.

4. **Multi-Pass Resolution**
   Pipelines support multiple resolution passes:
   - new info from Resolver A triggers running Resolver B
   - Resolver B can loop back to Resolver A if it discovers new key data

5. **Consolidation Stage**
   - Merge field-level provenance across resolvers
   - Apply final validation rules
   - Compute final confidence
   - Construct output domain model(s)

6. **Persistence Stage**
   - Write resolved models to Stashes
   - Store logs, provenance, conflict annotations

7. **Output**
   - Final model
   - Pipeline-level warnings
   - Complete provenance record
