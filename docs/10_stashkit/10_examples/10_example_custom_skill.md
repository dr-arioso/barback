
# Example: Writing a Custom Skill

```
from stashkit.skills import BaseSkill

class RegionSkill(BaseSkill):
    name = "region-skill"

    def execute(self, text):
        if "Kentucky" in text:
            return {
              "result": "US.Kentucky",
              "confidence": 0.9,
              "metadata": {"source": "rule"}
            }
        return {
          "result": None,
          "confidence": 0.0
        }
```

Add your new skill to a resolver via config or code.
