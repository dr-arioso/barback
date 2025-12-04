from __future__ import annotations
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional

class Item(BaseModel):
    """
    Generic inventory item.
    No assumptions about UPC, brand, volume, etc.
    Suitable for groceries, garnishes, fruit, tools, etc.
    """
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True
