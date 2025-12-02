from __future__ import annotations
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional
from uuid import uuid4, UUID

class Item(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    canonical_name: str
    aliases: List[str] = Field(default_factory=list)
    categories: List[str] = Field(default_factory=list)
    photo: Optional[str] = None
    notes: Optional[str] = None

    @model_validator(mode='before')
    def ensure_categories(cls, values):
        cats = values.get('categories')
        if not cats or len(cats) == 0:
            raise ValueError("Item must have at least one category")
        return values

class Product(Item):
    brand: str
    manufacturer: Optional[str] = None

    sku: Optional[str] = None
    upc: Optional[str] = None
    upc_photo: Optional[str] = None

    height_mm: float
    width_mm: float
    depth_mm: float
    weight_g: Optional[float] = None

    def resolve_upc(self, resolver_name: Optional[str] = None):
        from .resolvers import Resolver
        upc_resolver_cls = Resolver.get("upc")
        upc_resolver = upc_resolver_cls()
        upc_result = None
        if self.photo:
            upc_result = upc_resolver.resolve(self.photo)
        if not upc_result and resolver_name:
            next_resolver_cls = Resolver.get(resolver_name)
            next_resolver = next_resolver_cls()
            upc_result = next_resolver.resolve(self.photo)
        if not upc_result:
            manual_cls = Resolver.get("manual")
            manual_resolver = manual_cls()
            upc_result = manual_resolver.resolve(self.photo)
        self.upc = upc_result
        return self.upc
