from __future__ import annotations
from typing import Generic, TypeVar, List, Iterable, Optional, Callable

T = TypeVar("T")

class Stash(Generic[T]):
    """
    Simple iterable container of items/products/bottles.
    """

    def __init__(self, items: Optional[List[T]] = None):
        self.items: List[T] = items or []

    def __iter__(self) -> Iterable[T]:
        return iter(self.items)

    def add(self, item: T) -> None:
        self.items.append(item)

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [i for i in self.items if predicate(i)]
