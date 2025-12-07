# MetaDex API Schema (v1.2)

Each entity in the MetaDex may define an `api` block:

- `api.public_methods`: list of public, stable methods
- `api.internal_methods`: list of internal/private methods
- `api.properties`: list of notable properties or attributes
- `api.events`: list of named events or hooks

The compiler's normalization pass ensures that small YAML formatting
differences (especially in lists) do not change the semantic shape of
the compiled JSON.
