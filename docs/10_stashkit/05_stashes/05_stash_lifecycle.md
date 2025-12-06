
# Stash Lifecycle

1. **Initialization**
   - Load stash configuration (model type, index fields, persistence backend)
   - Create in-memory indexes
   - Optionally restore persisted state

2. **Insertion**
   - Validate model using schema or dataclass
   - Add object to primary storage
   - Index fields (e.g., by UPC, taxonomy path, name)
   - Record provenance (resolver → pipeline → stash)

3. **Lookup**
   - Query by:
     - primary key (ID)
     - secondary indexes
     - taxonomy path
     - alias
     - free text (if enabled)

4. **Update**
   - Apply partial or full replacement updates
   - Maintain index consistency

5. **Persistence**
   - Save entire stash or append journal entries
   - Backend could be:
     - Local JSON
     - SQLite
     - Remote HTTP API
     - Custom backend provided by StashPack

6. **Export**
   - Serialize objects + provenance for debugging or reporting
