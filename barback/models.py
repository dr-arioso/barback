from typing import Optional
from stashkit.models import Product

class Bottle(Product):
    labeled_volume_ml: int
    distiller: Optional[str] = None
    bottler: Optional[str] = None

    @property
    def manufacturer(self):
        return self.distiller or self.bottler or super().manufacturer
