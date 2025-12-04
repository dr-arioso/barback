from __future__ import annotations
from typing import Optional
from pydantic import Field
from .item import Item

class Product(Item):
    """
    Commercial product with UPC and manufacturer/brand metadata.
    """
    upc: Optional[str] = None
    brand: Optional[str] = None
    manufacturer: Optional[str] = None
    volume_ml: Optional[int] = None

    class Config:
        validate_assignment = True
