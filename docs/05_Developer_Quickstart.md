# Developer Quickstart

Everything you need to create your own Skills, Resolvers, and BoosterPacks.

---

# 🛠 Writing a Skill

```python
class NormalizeBrandSkill:
    skill_id = "brand.normalize"
    signal_type = "text"
    produces_fields = ["brand"]

    def apply(self, text, context):
        cleaned = text.strip().title()
        return {"brand": cleaned}
```

Registering:

```python
from stashkit import register_skill
register_skill(NormalizeBrandSkill())
```

---

# 🧠 Writing a Resolver

```python
class WidgetResolver:
    id = "widgets.resolver"
    domain = "widgets"
    required_fields = ["name"]

    skill_sequence = [
        "brand.normalize",
        "ask.user",
        "api.lookup"
    ]
```

Resolvers should:

- define required + optional fields  
- define skill sequence  
- optionally define termination rules  
- specify supported Dexes  

---

# 📦 Packaging a BoosterPack

```
mydomain/
  dex.yml
  resolver.py
  skills/
```

Installing:

```python
install_booster("mydomain")
```

---

Next up: **06_Workflow_Examples**.
