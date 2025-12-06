
# Template: Resolver Definition

```
id: bottle_resolver
type: resolver

order:
  - upc_skill
  - vision_skill
  - ocr_skill
  - classification_skill
  - manual_entry_skill

loopback_enabled: true
conflict_policy: confidence_weighted
```
