
# Resolver Lifecycle

1. **Initialization**
   - Resolver loads configuration, including Skill priority lists,
     retry parameters, and fallback strategies.

2. **Skill Selection**
   - Resolver chooses the next Skill based on:
     - declared order
     - capability flags
     - conditions (e.g., UPC detected → run UPCSkill next)

3. **Execution Loop**
   - Resolver calls each Skill
   - collects the result + confidence
   - records provenance
   - detects contradictions or missing fields

4. **Conflict Resolution**
   Resolvers merge multiple Skill outputs using:
   - confidence-weighted merges
   - last-writer-wins
   - schema validation
   - conflict flags for user review

5. **Fallback Logic**
   Resolvers may:
   - retry a Skill
   - invoke backup Skills
   - invoke manual entry
   - loop back if new information appears (e.g., UPC discovered late)

6. **Output**
   - validated model
   - full provenance
   - conflict annotations
