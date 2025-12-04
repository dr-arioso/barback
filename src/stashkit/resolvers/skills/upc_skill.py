from __future__ import annotations
from typing import Dict, Any, Optional
from stashkit.resolvers.base import ResolutionContext

class UPCSkill:
    """
    A StashSkill that does UPC-based enrichment.
    It assumes the resolver cares about UPC (Product-like semantics).
    """

    def apply_upc_skill(self, ctx: ResolutionContext) -> ResolutionContext:
        if not ctx.upc:
            return ctx
        upc_fields = self.lookup_upc(ctx.upc, ctx.fields)
        if upc_fields:
            ctx.fields.update(upc_fields)
        return ctx

    def lookup_upc(self, upc: str, current: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Override in concrete resolvers or provide a concrete implementation
        (e.g. using a local DB or a remote UPC service).
        """
        return None
