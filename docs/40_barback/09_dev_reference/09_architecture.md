
# Architecture Reference

```
User Input (CLI/UI/API)
        ↓
   Pipelines
        ↓
   Resolvers
        ↓
     Skills
        ↓
Classification Engine
        ↓
  BoozeDex (taxonomy + tags)
        ↓
 Persistence (StashKit Backend)
        ↓
    Inventory
```

Key properties:
- Inversion of control: Pipelines orchestrate Skills.
- Resolvers detect loopback triggers.
- Classification Engine maps messy descriptors → BoozeDex model.
