from __future__ import annotations
from typing import Dict, Any, Optional
from stashkit.resolvers.base import ResolutionContext

class PublicDBSkill:
    """
    A StashSkill to call one or more public databases, given a UPC and/or
    partial fields, and merge whatever they know into the context.
    """

    def apply_public_db_skill(self, ctx: ResolutionContext) -> ResolutionContext:
        if not ctx.upc:
            return ctx
        db_fields = self.lookup_public_dbs(ctx.upc, ctx.fields)
        if db_fields:
            ctx.fields = self.merge_fields(ctx.fields, db_fields)
        return ctx

    def lookup_public_dbs(self, upc: str, current: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Override in concrete resolvers to call OpenFoodFacts, etc.
        """
        return None

    def merge_fields(self, existing: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
        merged = dict(existing)
        for key, value in new.items():
            if value is None:
                continue
            if key not in merged or merged[key] in (None, "", []):
                merged[key] = value
        return merged
