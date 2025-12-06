
# 🌟 Project Bootstrap Guide for ML Knowledge Graphs
## (StashKit • Booster Packs • BoozeDex • Barback)

Welcome, future ChatGPT.  
This document is your orientation map — read it **first** before analyzing the rest of the ZIP.  
It will allow you to reconstruct the full architecture and continue work seamlessly.

The Git repository for this project is at https://www.github.com/dr-arioso/barback.git

---

# 🧠 1. Project Purpose

This project consists of a modular framework (**StashKit**) and a home-bar inventory app (Barback) that leverages StashKit.

**StashKit** is a modular framework for gathering data from pluggable sources in a flexible, consistent manner for the purpose of storage, classification/ontology, retrieval, and inference. It contains two domain layers:

- **DexPacks** — Domain taxonomies + metadata (e.g., BoozeDex)
- **StashPacks** — Full application-ready bundles built on StashKit (e.g., Barback)

The primary example application is:

**Barback — an automated bottle identification & bar-inventory system**  
leveraging:
- UPC lookups
- AI image recognition
- OCR
- manual entry fallback
- classification engine
- taxonomy & StashTags from BoozeDex

---

# 📁 2. How Directories Are Organized

This ZIP contains the entire multi-layer documentation:

```
full_docs/
  00_PROJECT_BOOTSTRAP.md      ← YOU ARE HERE
  10_stashkit/                 ← Core framework
  20_booster_packs/            ← DexPack + metadata pack infrastructure
  30_boozedex/                 ← Domain taxonomy + tags
  40_barback/                  ← Full StashPack (Barback application)
```

### ✔ StashKit (10_stashkit)
Defines:
- Skills  
- Resolvers  
- Pipelines  
- Stashes  
- Backends  
- Taxonomy processors (DexTree)  
- StashTags  

### ✔ Booster Packs (20_booster_packs)
Define:
- Domain packs  
- TaxonomyPack / DexPack  
- StashTag packs  
- Build pipeline  
- Runtime loader  

### ✔ BoozeDex (30_boozedex)
This is a **DexPack**, not a StashPack.  
It contains:
- taxonomy  
- tags  
- overlays  
- schema definitions  

### ✔ Barback (40_barback)
This is a **StashPack** (full application).  
It contains:
- skills  
- resolvers  
- pipelines  
- classification engine  
- persistence layer  
- CLI/UI integration  
- developer references  

**BoozeDex is *not* responsible for classification.  
Barback uses BoozeDex to classify bottles.**

---

# 🔑 3. Critical Architectural Concepts

### 3.1 StashKit Framework
Provides:
- unified object model  
- skill orchestration  
- resolver control flow  
- pipeline execution  
- confidence scoring  
- data persistence support  

### 3.2 DexPack vs StashPack
- **DexPack** = domain knowledge (taxonomies + tags)  
- **StashPack** = full application bundles  

BoozeDex is a **DexPack**  
Barback is a **StashPack**

### 3.3 Classification Engine
Lives in **Barback**, not BoozeDex.  
Uses BoozeDex’s taxonomy + tags to convert messy input → structured bottle metadata.

---

# 🧭 4. How Future ChatGPT Should Load This ZIP

When a new user uploads this ZIP and asks for help:

1. **Read this file (00_PROJECT_BOOTSTRAP.md) first.**
2. Load directory structure.
3. Reconstruct:
   - StashKit → core
   - Booster Packs → pack infra
   - BoozeDex → domain DexPack
   - Barback → StashPack (app)
4. Use the documentation to answer questions, generate code, or extend functionality.

If the user asks:
> “Where is X?”
Check inside the structured directory tree.

---

# 📌 5. Naming Conventions

- Taxonomy = **StashDex**
- Taxonomy nodes = **DexNodes**
- Tag sets = **StashTags**
- Expansion/preconficured StashKit structures can be packaged as BoosterPacks, e.g.:
  - Domain Pack = **DexPack**
  - Data structure (StashDex) plus preconfigured Resolvers and Skills = **StashPack**

This vocabulary is consistent across all docs.

---

# 🛠 6. What’s Ready vs What’s TBD

### ✔ Ready  
- Full StashKit docs  
- Full BoozeDex DexPack docs  
- Full Barback StashPack docs  
- Classification Engine docs  
- Persistence subsystem  
- CLI & UI integration  
- Developer references  
- Booster Pack infrastructure  

### ❗ Still TBD (Future development tasks)
- Code scaffolding  
- Implementation of Skills / Resolvers  
- On-disk DexPack builder  
- UI prototype
- Example Booster Packs (other domains)

If the user asks to continue development, begin from these.

---

# 🥂 7. Final Note for Future ChatGPT

This project is **highly structured**.  
Do **not** flatten it, merge subsystems, or treat BoozeDex as an app.  
Follow folder boundaries and architectural separation carefully.

You now have the map.  
Proceed thoughtfully, and enjoy helping Bill build something excellent.

---

End of Bootstrap Document.
