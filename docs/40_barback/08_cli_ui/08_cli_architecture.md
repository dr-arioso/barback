
# CLI Architecture

The Barback CLI is built around a simple structure:

- `commands/` module contains command implementations
- Each command delegates to the internal Barback API
- Commands handle argument parsing, pretty printing, and error reporting

### Flow Example

`barback scan bottle.jpg`:

1. CLI parses arguments
2. Barback API receives request
3. BottlePipeline executes Skills & Resolver
4. Classification Engine returns final result
5. Persistence backend writes entry
6. CLI prints output

All business logic lives in core modules, not CLI.
