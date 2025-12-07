# Getting Started with StashKit

Welcome to your first hands-on experience with StashKit.  
This guide walks you through installation, basic usage, BoosterPack installation, and what actually happens when you call `fetch()`.

---

## 📦 Installation

StashKit can be installed like any Python package:

```bash
pip install stashkit
```

You will typically work with two imports:

```python
from stashkit import fetch, install_booster
```

- `fetch()` is the high-level convenience function for resolving user requests.
- `install_booster()` loads domain BoosterPacks that give StashKit its intelligence.

---

## 🚀 Your First Resolution

```python
from stashkit import fetch

item = fetch("sony nois canceling hedphones")
print(item.canonical_name)
```

What just happened?

1. StashKit Core selected a Resolver appropriate for product-like inputs.
2. The Resolver orchestrated multiple Skills:
   - string cleanup
   - alias normalization
   - similarity matching
3. Skills proposed candidate fields.
4. Resolver merged those proposals.
5. StashDex enriched the interpretation (brand, product category, model family).
6. You received a structured entity.

---

## 🧩 Installing Your First BoosterPack

BoosterPacks give StashKit domain knowledge.

```python
from stashkit import install_booster

install_booster("tinybar")
```

This installs:

- **BoozeDex** (a spirits ontology)
- **BottleResolver**
- **Spirits-related Skills**

Now you can do:

```python
item = fetch("espolon repsado")
print(item.brand)       # Espolón
print(item.type)        # Tequila Reposado
print(item.agave_type)  # Blue Weber (inferred)
```

---

## 🧠 What `fetch()` Actually Does (High-Level)

```mermaid
flowchart TD
    A[fetch()] --> B[Resolver Selected]
    B --> C[Skill Chain Executed]
    C --> D[StashDex Consulted]
    D --> E[Structured Entity Returned]
```

---

## 🎯 Summary

- Install StashKit.
- Install any BoosterPacks you need.
- Call `fetch()` and enjoy structured, enriched results.

Ready for deeper understanding? Continue to **03_Concepts**.
