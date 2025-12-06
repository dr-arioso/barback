
# Pipeline Design Principles

## 1. Composability
Pipelines are compositions of resolvers, not replacements for them. Each stage
should be modular and replaceable.

## 2. Idempotence
Running a pipeline twice on the same input should yield the same result,
unless configuration explicitly allows nondeterministic behavior.

## 3. Transparency
All decisions, confidences, and intermediate results must be logged for
provenance and debugging.

## 4. Minimal Domain Knowledge
Pipelines should not encode domain logic; this belongs in Resolvers or StashPacks.

## 5. Safety
Pipelines enforce:
- error boundaries
- structured exceptions
- data validation
