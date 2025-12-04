from __future__ import annotations
from typing import Optional, Dict
from pydantic import Field
from stashkit.models.product import Product

class Bottle(Product):
    """
    Barback-specific specialization of Product.
    """
    abv_percent: Optional[float] = None
    category: Optional[str] = None           # e.g. "Vodka", "Gin"
    distiller: Optional[str] = None
    bottler: Optional[str] = None
    dimensions_cm: Optional[Dict[str, float]] = None  # {"height": 30, ...}

    class Config:
        validate_assignment = True

    @property
    def manufacturer(self) -> Optional[str]:
        return self.distiller or self.bottler or self.brand or self._manufacturer()

    def _manufacturer(self) -> Optional[str]:
        return self.manufacturer  # simple fallback; can be refined
