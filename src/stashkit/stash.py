from __future__ import annotations
from typing import Generic, TypeVar, Dict, List, Optional
from .models import Item
from .datastores import Datastore
from .resolvers import Resolver

T = TypeVar("T", bound=Item)

class Stash(Generic[T]):
    def __init__(self, resolver_name: Optional[str] = None):
        self._items: Dict[str, T] = {}
        self.resolver_name = resolver_name

    def add(self, item: T):
        if item.id.hex in self._items:
            raise ValueError(f"Duplicate ID {item.id}")
        self._items[item.id.hex] = item

    def get(self, id: str) -> T:
        return self._items[id]

    def list(self) -> List[T]:
        return list(self._items.values())

    def find(self, **query) -> List[T]:
        results = []
        for item in self._items.values():
            if all(getattr(item, k, None) == v for k, v in query.items()):
                results.append(item)
        return results

    def __iter__(self):
        return iter(self._items.values())

    def output(self, datastore_name: str):
        store_cls = Datastore.get(datastore_name)
        store = store_cls()
        return store.save(self)

    def resolve_item(self, input_data):
        if not self.resolver_name:
            raise RuntimeError("No resolver configured")
        resolver_cls = Resolver.get(self.resolver_name)
        resolver = resolver_cls()
        return resolver.resolve(input_data)
