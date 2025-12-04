from __future__ import annotations
from typing import Dict, Any
from stashkit.resolvers.base import ResolutionContext
from stashkit.resolvers.manual import ManualResolver

class KeyboardEntrySkill:
    """
    A StashSkill that delegates to a ManualResolver to
    interactively fill or confirm fields via keyboard.
    """

    manual: ManualResolver  # expected to be provided by the BaseResolver

    def apply_keyboard_entry_skill(self, ctx: ResolutionContext) -> ResolutionContext:
        if self.manual is None:
            return ctx
        ctx.fields = self.manual.fill_missing(ctx.fields)
        return ctx
