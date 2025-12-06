
# Booster Pack Lifecycle

1. **Installation**
   - user installs via pip or drops a folder into their project

2. **Discovery**
   - StashKit scans `booster_packs/` directory
   - loads each `booster.yaml`

3. **Loading**
   - taxonomies compiled
   - tags registered
   - Skills, Resolvers, Pipelines mapped to names
   - default configuration merged into global config

4. **Activation**
   - user selects a Booster Pack explicitly or implicitly:
     ```
     from stashkit import activate_pack
     activate_pack("boozedex")
     ```

5. **Runtime**
   - pack provides domain logic to Skills / Resolvers
   - pipelines run with enriched semantics
   - Stashes gain domain-specific indexing

6. **Unloading / Switching**
   - pack may be disabled or replaced at runtime
