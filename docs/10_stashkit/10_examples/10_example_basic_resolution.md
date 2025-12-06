
# Example: Basic Product Resolution

This example shows how to resolve a simple product using a single Resolver.

```
from stashkit.resolvers import ProductResolver
from stashkit.pipelines import Pipeline

resolver = ProductResolver()
pipeline = Pipeline(resolvers=[resolver])

result = pipeline.run("Cointreau")
print(result.model)
```

Output might include:
- resolved classification (e.g., liqueurs.fruit.orange.triple_sec)
- inferred tags
- confidence scores
- provenance log
