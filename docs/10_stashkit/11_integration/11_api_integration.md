
# Integration with Third‑Party APIs

StashKit provides Skills and Resolvers that integrate with:

- Vision APIs (OpenAI, Google Cloud Vision, Azure Vision)
- UPC databases (Open Product Data, OpenFoodFacts, commercial APIs)
- GS1 GPC codes (via lookup tables or external APIs)
- Ingredient or cocktail metadata APIs (TheCocktailDB, etc.)

## Example: Vision API integration

```
class AIVisionSkill(BaseSkill):
    def execute(self, image_path):
        response = openai.vision.extract_labels(image_path)
        return {
            "result": response.labels,
            "confidence": response.confidence,
            "metadata": {"provider": "openai"}
        }
```

## Rate limiting and best practices

- Respect API provider rate limits  
- Cache lookups  
- Store results in Stashes for reuse  
- Provide fallbacks if API keys are missing  
