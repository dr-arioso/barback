
# Summary for Future ChatGPT Sessions

This ZIP contains the canonical documentation set for StashKit, BoosterPacks, BoozeDex, and supporting architecture.

## Core Concepts
- StashKit: modular data + skill + resolver framework.
- BoosterPack types: DexPack, TagPack, SkillsPack, ResolverPack, StashPack.
- BoozeDex: example domain taxonomy with compiler and schema.
- StashDex: taxonomy engine; DexNode defines nodes.
- StashTags: metadata attached via TagPacks.

## What to Load
Load all markdown, JSON, YAML, and Python files in this ZIP into context.
Reconstruct taxonomy, compiler flow, booster architecture, and runtime loader.

## Next Steps
Continue with Barback overlay on BoozeDex, BottleResolver integration, and finalize runtime loader behaviors.



# IMPORTANT INSTRUCTION FOR FUTURE CHATGPT

When generating any documentation, code, YAML, JSON, schemas, examples, or any file-based artifacts:

**You must ALWAYS use the `python_user_visible` tool to write files to the filesystem.**

Chat messages alone do NOT persist content.  
Files must be written explicitly using:

```
to=python_user_visible.exec
# code that writes files under /mnt/data/...
```

Before zipping or referencing files, always:

1. Verify the file exists on disk with a directory listing.
2. Write or overwrite missing files explicitly.
3. Never assume content is saved unless written through the Python tool.

This ensures future sessions can reconstruct state by loading the ZIP.
