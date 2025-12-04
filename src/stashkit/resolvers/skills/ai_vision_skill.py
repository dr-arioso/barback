from __future__ import annotations
from typing import Dict, Any
from stashkit.resolvers.base import ResolutionContext

class AIVisionSkill:
    """
    A StashSkill providing an AI-Vision-based resolution step.
    The actual model invocation is left to subclasses.
    """

    def apply_ai_vision_skill(self, ctx: ResolutionContext) -> ResolutionContext:
        if not ctx.image_path:
            return ctx
        new_fields = self.infer_from_image(ctx.image_path, ctx.fields)
        if new_fields:
            ctx.fields = self.merge_fields(ctx.fields, new_fields)
        return ctx

    def infer_from_image(self, image_path: str, current: Dict[str, Any]) -> Dict[str, Any]:
        """
        Override in concrete resolvers to call Tesseract, OpenCV, Google Vision,
        OpenAI Vision, etc., and return additional/updated fields.
        """
        return {}

    def merge_fields(self, existing: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
        merged = dict(existing)
        for key, value in new.items():
            if value is None:
                continue
            if key not in merged or merged[key] in (None, "", []):
                merged[key] = value
        return merged
