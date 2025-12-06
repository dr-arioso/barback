
# Build Pipeline Design Principles

## 1. Human‑Editable → Machine‑Efficient
Taxonomies should remain readable and maintainable by humans.
The builder converts them into optimized runtime formats.

## 2. Deterministic Output
The same Booster Pack must always compile into identical artifacts.
No randomness. No environment‑dependent variation.

## 3. Strict Validation
The build must fail loudly on:
- missing parents  
- invalid ordering  
- ambiguous paths  
- inconsistent tag definitions  

## 4. Extensibility
Custom Booster Packs may:
- add new build phases
- define custom schemas
- bundle custom compilers

## 5. Debuggability
Each build produces:
- a manifest  
- a compilation log  
- optional debug dumps of DexTrees  
