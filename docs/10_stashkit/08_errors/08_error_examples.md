
# Error Examples

## 1. SkillError (e.g., UPCSkill)
```
raise SkillExecutionError(
    message="Failed to decode UPC",
    context={"skill": "upc_skill", "image_resolution": "low"},
    hint="Try a sharper or closer photo"
)
```

## 2. ResolverConflictError
```
raise ResolverConflictError(
    message="Conflicting ABV values",
    context={"resolver": "bottle_resolver", "values": [40, 42]},
    hint="User review required"
)
```

## 3. StashValidationError
```
raise StashValidationError(
    "Bottle model missing required field: `classification`"
)
```

## 4. PipelineExecutionError
```
raise PipelineExecutionError(
    "Resolver chain stopped prematurely",
    context={"pipeline": "bottle_pipeline", "last_resolver": "ocr_resolver"}
)
```
