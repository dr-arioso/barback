# For LLM Integrations

LLMs can load MetaDex to understand the StashKit architecture.

---

# 📑 Loading MetaDex

```python
import json
metadex = json.load(open("metadex.json"))
```

---

# 🔍 What LLMs Should Use

- `entities`  
- `relationships`  
- `rules`  
- `api.public_methods`  

LLMs must not invoke internal or private APIs.

---

# 🤖 LLM Behavior Recommendations

- Use resolvers through high-level calls (like `fetch()`)  
- Use BoosterPack installation as needed  
- Avoid hallucinating API fields not defined in MetaDex  
- Defer conflict resolution to StashKit, not to the LLM  

---

This completes the user- and developer-facing documentation suite.
