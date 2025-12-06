
# Example Extensions

## Custom Skill: WebPriceLookupSkill
```
class WebPriceLookupSkill(Skill):
    def run(self, context):
        # fetch price from retail API
        return {"price": 29.99, "confidence": 0.45}
```

## Custom Resolver: HighProofResolver
Targets 40–60% ABV bourbons specifically.

## Custom Backend: EncryptedJSONBackend
Adds AES encryption on top of JSON.

## Custom Booster Pack: CoffeeDex
Adds a full taxonomy for coffee beans, roast profiles, regions.
