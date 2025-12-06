
# Errors Subsystem Overview

The **Errors subsystem** defines typed exceptions used throughout StashKit.
Errors provide structured, predictable failure modes across Skills, Resolvers,
Pipelines, and Stashes.

StashKit errors follow principles of:

- **Clarity** — precise meaning, minimal ambiguity  
- **Typed categorization** — each subsystem defines its own error classes  
- **Recoverability** — failures include enough context for resolution  
- **Logging integration** — all errors designed for structured logs  
- **Uniform handling** — pipelines treat errors consistently  
