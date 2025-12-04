from __future__ import annotations
from typing import Iterable
from stashkit.stash.stash import Stash
from barback.models import Bottle

class BottleStash(Stash[Bottle]):
    """
    Represents the user's home bar inventory.
    """

    def list_brands(self) -> Iterable[str]:
        return sorted({b.manufacturer for b in self.items if b.manufacturer})

    def list_categories(self) -> Iterable[str]:
        return sorted({b.category for b in self.items if b.category})
