# Bottle Resolver

Barback assembles skills in its preferred order:

```python
resolver = BottleResolver(
    model=Bottle,
    skills=[
        UPCSkill(),
        PublicDBSkill(),
        AIVisionSkill(),
        KeyboardEntrySkill(),
    ]
)
```

BottleResolver is domain-specific but powered by StashKit's generic infrastructure.

