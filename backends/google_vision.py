from backends.base import BackendInterface
from backends.simple_backend import BottleResolver
from google.cloud import vision
from google.oauth2 import service_account
from typing import Optional, Dict, Any
import logging
import os

logger = logging.getLogger(__name__)

class GoogleVisionBackend(BackendInterface):
    def __init__(self, service_account_file: Optional[str] = None):
        super().__init__(api_key=None)
        self.service_account_file = service_account_file
        self.client = None
        self.simple_fallback = BottleResolver()
        if service_account_file and os.path.exists(service_account_file):
            credentials = service_account.Credentials.from_service_account_file(service_account_file)
            self.client = vision.ImageAnnotatorClient(credentials=credentials)

    def resolve_from_barcode(self, barcode: str) -> Optional[Dict[str, Any]]:
        return self.simple_fallback.resolve_from_barcode(barcode)

    def resolve_from_image(self, image_path: str) -> Optional[Dict[str, Any]]:
        if not self.client:
            logger.warning("GoogleVision client not initialized, using BottleResolver fallback")
            return self.simple_fallback.resolve_from_image(image_path)
        from google.cloud.vision_v1 import types
        with open(image_path, 'rb') as f:
            content = f.read()
        image = vision.Image(content=content)
        response = self.client.text_detection(image=image)
        text = response.text_annotations[0].description if response.text_annotations else ""
        result = self.simple_fallback.resolve_from_image(image_path)
        return result

    def fetch_dimensions_from_web(self, query: str) -> Optional[Dict[str, float]]:
        return self.simple_fallback.fetch_dimensions(query)
