# Resolvers

Resolvers translate raw input (images, text) into structured Item/Product metadata.

## ProductResolver Base Class

Barback also includes a home-bar–specific abstract base class for product resolution:

```python
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import logging
import requests

logger = logging.getLogger(__name__)

class ProductResolver(ABC):
    """Abstract base class for all product resolvers."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    @abstractmethod
    def resolve_from_barcode(self, barcode: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def resolve_from_image(self, image_path: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def fetch_dimensions(self, query: str) -> Optional[Dict[str, float]]:
        raise NotImplementedError
```

## StashKit Resolver Base Class

* Maintains a registry `_registry` for all resolvers.
* Must implement `resolve(input_data)`.

### Example Built-in Resolvers

* `UPCResolver` – attempts to resolve UPC codes from images.
* `ManualResolver` – manual fallback resolver.

## Resolver Usage

```python
resolver_cls = Resolver.get("upc")
resolver = resolver_cls()
result = resolver.resolve(input_data)
```

## Future Enhancements

* Parallel resolver execution
* Majority-vote aggregation
* Cloud-based resolver integration
