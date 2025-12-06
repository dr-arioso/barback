
# Resolvers Subsystem Overview

Resolvers coordinate the execution of Skills, perform conflict resolution,
handle fallback logic, validate outputs, and ultimately produce structured
domain models. Resolvers are the “brains” of StashKit pipelines.

Resolvers do **not** contain domain knowledge; they orchestrate Skills and
apply validation, merging, and retry policies.
