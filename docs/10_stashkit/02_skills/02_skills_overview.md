
# Skills Subsystem Overview

Skills are the smallest units of intelligence in StashKit.  
A Skill performs a single inference task on an input and returns:

- A structured result
- A confidence value between 0.0 and 1.0
- Optional metadata (warnings, provenance, timing)

Skills **never** orchestrate other skills; this is handled by Resolvers.
