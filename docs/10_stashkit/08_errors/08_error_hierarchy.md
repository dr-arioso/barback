
# Error Hierarchy

All StashKit errors inherit from `StashKitError`.

```
StashKitError
├── SkillError
│     ├── SkillConfigError
│     └── SkillExecutionError
├── ResolverError
│     ├── ResolverConfigError
│     └── ResolverConflictError
├── PipelineError
│     ├── PipelineConfigError
│     └── PipelineExecutionError
├── StashError
│     ├── StashValidationError
│     ├── StashPersistenceError
│     └── StashIndexError
└── ConfigError
```

This hierarchy guarantees that subsystems can catch and handle errors at the
granularity they need.
