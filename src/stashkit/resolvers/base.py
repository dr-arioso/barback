from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, TypeVar, Generic

from stashkit.resolvers.manual import ManualResolver

T = TypeVar("T")  # Concrete model type (Item/Product/Bottle/etc.)

class ResolutionContext:
    """
    Shared context passed between StashSkills in the pipeline.
    """
    def __init__(self,
                 upc: Optional[str] = None,
                 image_path: Optional[str] = None,
                 fields: Optional[Dict[str, Any]] = None):
        self.upc = upc
        self.image_path = image_path
        self.fields: Dict[str, Any] = fields or {}

class BaseResolver(ABC, Generic[T]):
    """
    Template-method resolver that orchestrates StashSkills in a fixed order:

      1. UPCSkill (if skill is present and UPC available)
      2. PublicDBSkill (if present, and UPC available)
      3. AIVisionSkill (if image available and skill present)
      4. KeyboardEntrySkill / ManualResolverSkill (if configured)

    The actual "skills" are provided by mixins that define
    methods like `apply_upc_skill`, `apply_public_db_skill`, etc.
    """

    def __init__(self, manual: Optional[ManualResolver] = None):
        self.manual = manual

    # ---------- Public entrypoint ----------

    def resolve(
        self,
        *,
        upc: Optional[str] = None,
        image_path: Optional[str] = None,
        allow_manual: bool = True,
    ) -> T:
        ctx = ResolutionContext(upc=upc, image_path=image_path, fields={})

        # 1) UPC
        if ctx.upc and hasattr(self, "apply_upc_skill"):
            ctx = self.apply_upc_skill(ctx)  # type: ignore[attr-defined]

        # 2) Public DB (for UPC-backed products)
        if ctx.upc and hasattr(self, "apply_public_db_skill"):
            ctx = self.apply_public_db_skill(ctx)  # type: ignore[attr-defined]

        # 3) AI Vision
        if ctx.image_path and hasattr(self, "apply_ai_vision_skill"):
            ctx = self.apply_ai_vision_skill(ctx)  # type: ignore[attr-defined]

        # 4) Manual completion / keyboard entry
        if allow_manual and self.manual is not None:
            # Let the manual resolver work over the aggregate fields
            ctx.fields = self.manual.fill_missing(ctx.fields)

        # Build final model
        return self.build_item(ctx.fields)

    # ---------- Abstract method to build model ----------

    @abstractmethod
    def build_item(self, fields: Dict[str, Any]) -> T:
        """Turn a dict of fields into the final Pydantic model."""
        raise NotImplementedError


class ItemResolver(BaseResolver[T], ABC):
    """
    For Items without inherent UPC semantics.
    Does not require UPC-specific skills.
    """
    pass


class ProductResolver(BaseResolver[T], ABC):
    """
    For Products where UPC semantics make sense.
    Typically combined with UPCSkill + PublicDBSkill StashSkills.
    """
    pass
