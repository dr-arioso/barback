
# SkillsPack Template

## Overview
SkillsPacks provide new Skills for StashKit resolvers.

## Directory Structure
```
skillspack-example/
  booster.yaml
  skills/
    example_skill.py
```

## booster.yaml
```yaml
name: skillspack-example
version: 0.1.0
type: skillspacks
entry_points:
  skills: skills/
dependencies: []
```

## skills/example_skill.py
```python
from stashkit.skills import BaseSkill

class ExampleSkill(BaseSkill):
    name = "example-skill"

    def execute(self, input):
        return {"result": "demo", "confidence": 1.0}
```

## Notes
- Skills must subclass BaseSkill.
- Skill names should be unique.
