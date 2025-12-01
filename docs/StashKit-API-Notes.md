# StashKit API Notes

## Overview
StashKit acts as the abstraction layer between:
- Input image(s)
- Resolver(s)
- Output formatter(s)
- Metadata normalization

StashKit should be importable as:

```python
from stashkit import Stash, ResolverBase, OutputBase
```

And support simple top-level usage:

```python
stash = Stash(resolver="google")
result = stash.process("photos/input.jpg", output="json,csv")
```

## Minimum Interfaces

### Base Resolver
```python
class ResolverBase:
    name: str

    def resolve(self, image_path: str) -> dict:
        raise NotImplementedError
```

### Output Plugin
```python
class OutputBase:
    name: str
    file_extension: str

    def generate(self, results: list[dict], output_dir: str) -> str:
        raise NotImplementedError
```
