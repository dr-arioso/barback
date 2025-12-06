
# Cocktail Roles Overlay

Cocktail roles describe *how* an ingredient behaves in a drink.

```
cocktail_roles:
  base_spirit:
    description: Primary alcoholic component
  modifier:
    description: Adds flavor, sweetness, or bitterness
  lengthener:
    description: Increases volume with low ABV impact
  sour_agent:
    description: Provides acidity (e.g., lemon, lime)
  sweetener:
    description: Provides sweetness (e.g., syrups, juices)
  foaming_agent:
    description: Adds foam or texture (e.g., egg white, aquafaba)
```

Examples:
- Gin → base_spirit  
- Aperol → modifier  
- Lemon juice → sour_agent  
- Egg white → foaming_agent  
