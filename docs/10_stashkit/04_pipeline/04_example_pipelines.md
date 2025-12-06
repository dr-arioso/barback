
# Example Pipelines

## 1. Barback Bottle Pipeline
Stages:
1. Preprocess image
2. Run BottleResolver
3. Run ClassificationResolver
4. Validate Bottle model
5. Persist to BottleStash

## 2. Text-Only Product Pipeline
1. Normalize text
2. NameOnlyResolver
3. Taxonomy classification
4. Persist to ProductStash

## 3. Multi-Resolver Metadata Pipeline
1. VisionSkill → Resolver A
2. NLPSkill → Resolver B
3. Merge outputs
4. Construct Metadata model
