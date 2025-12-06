
# Example Resolvers

## 1. BottleResolver (Barback)
Pipeline:
1. UPCDetectionSkill
2. UPCSkill
3. VisionSkill
4. OCRSkill
5. ClassificationSkill
6. ManualEntrySkill

Resolver uses loopback if VisionSkill later discovers a UPC.

## 2. ProductResolver (StashKit)
Generic metadata resolver for arbitrary product taxonomies.

## 3. NameOnlyResolver
Use textual name to guess taxonomy and metadata.

## 4. ManualResolver
User-only override resolver.
