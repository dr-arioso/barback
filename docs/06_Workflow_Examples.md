# Workflow Examples

These examples illustrate real resolutions performed by StashKit + BoosterPacks.

---

# 🎧 Example 1 — Electronics

```python
item = fetch("sony nois canceling hedphones")
print(item.brand)
print(item.category)
print(item.model)
```

---

# 🍎 Example 2 — AirPods

```python
install_booster("electronics.basic")
item = fetch("apple air pods pro")
print(item.brand)      # Apple
print(item.category)   # Earbuds
print(item.series)     # AirPods Pro
```

---

# 👤 Example 3 — User-Assisted Resolution

```python
class AskUserSkill:
    skill_id = "ask.user"
    signal_type = "user"
    produces_fields = ["missing"]

    def apply(self, field, context):
        return { field: input(f"Enter {field}: ") }
```

Resolvers can include fallback skills like this when automated interpretation is insufficient.

---

Continue to **07_For_ML_use**.
