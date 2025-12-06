
# Skills Integration

Barback uses several core skills:

- `UPCScanSkill`
- `UPCLookupSkill`
- `AIVisionSkill`
- `OCRSkill`
- `ManualEntrySkill`
- `ClassificationSkill` (internal wrapper around the classification engine)

Skills register automatically and are orchestrated through Resolvers and Pipelines.

Integration notes:
- Skills receive BoozeDex schema + taxonomy references
- Skills return structured partial models with confidence values
