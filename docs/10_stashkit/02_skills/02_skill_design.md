
# Designing Skills

## Principles
- **Atomic**: Perform exactly one inference task.
- **Stateless**: Avoid holding intermediate state between calls.
- **Configurable**: Use external configuration for APIs or thresholds.
- **Composable**: Work well when chained by a Resolver.

## Recommended Structure
```
class UPCSkill(BaseSkill):
    name = "upc-skill"

    def execute(self, image):
        ...
        return {
            "result": upc_code,
            "confidence": 0.92,
            "metadata": {...}
        }
```
