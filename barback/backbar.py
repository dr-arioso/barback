from stashkit.stash import Stash
from .models import Bottle

class BackBar(Stash[Bottle]):
    """Domain-specific stash for bottles"""

    def total_volume(self) -> float:
        return sum(b.labeled_volume_ml for b in self)
