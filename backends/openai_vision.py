from backends.base import BackendInterface
from backends.simple_backend import BottleResolver
from typing import Optional, Dict, Any
import logging
import openai

logger = logging.getLogger(__name__)

class OpenAIVisionBackend(BackendInterface):
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key=api_key)
        if api_key:
            openai.api_key = api_key
        self.simple_fallback = BottleResolver()

    def resolve_from_barcode(self, barcode: str) -> Optional[Dict[str, Any]]:
        return self.simple_fallback.resolve_from_barcode(barcode)

    def resolve_from_image(self, image_path: str) -> Optional[Dict[str, Any]]:
        if not openai.api_key:
            logger.warning("OpenAI API key not set, using BottleResolver fallback")
            return self.simple_fallback.resolve_from_image(image_path)
        from core.pipeline import ocr_image_text
        text = ocr_image_text(image_path)
        prompt = f"Identify brand, volume (mL), and category from this text: '{text}'"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response['choices'][0]['message']['content']
        except Exception as e:
            logger.warning(f"OpenAI API failed: {e}, using fallback")
            return self.simple_fallback.resolve_from_image(image_path)
        result = self.simple_fallback.resolve_from_image(image_path)
        # Optionally parse OpenAI answer and override fallback
        return result

    def fetch_dimensions_from_web(self, query: str) -> Optional[Dict[str, float]]:
        return self.simple_fallback.fetch_dimensions(query)
