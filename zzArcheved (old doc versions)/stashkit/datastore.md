# StashKit Datastore

StashKit supports pluggable persistence backends.

## StorageBackend Interface
```python
class StorageBackend(ABC, Generic[T]):
    @abstractmethod
    def load(self) -> list[dict]:
        ...

    @abstractmethod
    def save(self, items: list[dict]) -> None:
        ...
```

## JSON Backend

Supports storing Product or Item data as JSON documents. Domain-specific reconstruction happens in the application layer (e.g., Barback).

