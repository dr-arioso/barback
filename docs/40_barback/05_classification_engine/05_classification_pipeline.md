
# Classification Pipeline

The classification engine runs in the following stages:

1. **Normalize Input**
   - lowercase
   - remove punctuation
   - tokenize
   - extract numeric cues (ABV, volume)

2. **Candidate Extraction**
   - direct taxonomy matches
   - synonym/alias matches
   - fuzzy text matches
   - weighted keyword extraction

3. **Scoring**
   - keyword relevance
   - feature strength (mentions of style, category, ABV)
   - pack-level overrides
   - source confidence (UPC > AI > OCR > manual input)

4. **Conflict Resolution**
   - competing categories (e.g., gin vs. flavored vodka)
   - multiple style candidates
   - ambiguous liqueurs (triple sec vs. curaçao)

5. **Final Classification**
   - best-path selection
   - StashTag inference
   - confidence assignment
   - provenance log generation
