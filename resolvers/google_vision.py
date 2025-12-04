from __future__ import annotations
from typing import Dict, Any
import logging
import os

from barback.resolvers.bottle_resolver import BottleResolver

logger = logging.getLogger(__name__)

try:
    from google.cloud import vision
    from google.oauth2 import service_account
except ImportError:
    vision = None
    service_account = None

class GoogleVisionResolver(BottleResolver):
    """
    BottleResolver variant that uses Google Vision for the AIVisionSkill step.
    """

    def __init__(self, service_account_file: str | None = None, **kwargs):
        super().__init__(**kwargs)
        self.client = None
        if service_account_file and vision and service_account:
            if os.path.exists(service_account_file):
                creds = service_account.Credentials.from_service_account_file(
                    service_account_file
                )
                self.client = vision.ImageAnnotatorClient(credentials=creds)
            else:
                logger.warning(f"Google Vision service account file not found: {service_account_file}")

    def infer_from_image(self, image_path: str, current: Dict[str, Any]) -> Dict[str, Any]:
        if not self.client:
            logger.warning("[GoogleVisionResolver] No Vision client; falling back to BottleResolver placeholder")
            return super().infer_from_image(image_path, current)

        with open(image_path, "rb") as f:
            content = f.read()

        image = vision.Image(content=content)
        response = self.client.text_detection(image=image)
        if response.error.message:
            logger.warning(f"Google Vision error: {response.error.message}")
            return super().infer_from_image(image_path, current)

        text = response.text_annotations[0].description if response.text_annotations else ""
        logger.info(f"[GoogleVisionResolver] OCR text length={len(text)}")
        # For now, this just logs; you can reuse BottleResolver heuristics later.
        return {}
