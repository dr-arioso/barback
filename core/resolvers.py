
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import logging
import requests

logger = logging.getLogger(__name__)

class ProductResolver(ABC):
    """
    Abstract base class for all product resolvers.
    Subclasses must implement resolve_from_barcode, resolve_from_image, and fetch_dimensions.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    @abstractmethod
    def resolve_from_barcode(self, barcode: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def resolve_from_image(self, image_path: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def fetch_dimensions(self, query: str) -> Optional[Dict[str, float]]:
        raise NotImplementedError


class BottleResolver(ProductResolver):
    """
    Default resolver (previously BottleResolver).
    Provides local brand matching, OCR volume/category extraction, and web lookup fallback.
    """

    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        from core.brand_matching import resolve_brand, load_brands, save_brands
        self.resolve_brand = resolve_brand
        self.brand_list = load_brands()
        if not self.brand_list:
            self.brand_list = [
                "Absolut","Smirnoff","Grey Goose","Ketel One","Bombay Sapphire",
                "Tanqueray","Bacardi","Mount Gay","Havana Club","Patron",
                "Jose Cuervo","Jack Daniel's","Johnnie Walker","Jim Beam",
                "Grand Marnier","Cointreau","Torres","Campari","Aperol"
            ]

    def resolve_from_barcode(self, barcode: str) -> Optional[Dict[str, Any]]:
        logger.info(f"Lookup barcode {barcode} (placeholder)")
        return None

    def resolve_from_image(self, image_path: str) -> Optional[Dict[str, Any]]:
        from core.pipeline import ocr_image_text
        text = ocr_image_text(image_path)
        brand = self.resolve_brand(text, silent=True)
        volume_ml = self.extract_volume_from_text(text)
        category = self.classify_category_from_text(text)
        dims = self.fetch_dimensions(brand or "")
        logger.info(f"Identified {brand} {volume_ml}ml {category} dims={dims}")
        return {"brand": brand, "volume_ml": volume_ml, "category": category, "dimensions_cm": dims}

    def fetch_dimensions(self, query: str) -> Optional[Dict[str, float]]:
        if not query:
            return None
        # Default web lookup: OpenFoodFacts -> OpenProductData
        try:
            r = requests.get(f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&json=true", timeout=6)
            r.raise_for_status()
            data = r.json()
            return {"height_cm": None, "width_cm": None, "depth_cm": None}
        except Exception:
            try:
                r2 = requests.get(f"https://api.openproductdata.com/products?query={query}", timeout=6)
                r2.raise_for_status()
                data2 = r2.json()
                return {"height_cm": None, "width_cm": None, "depth_cm": None}
            except Exception:
                return None

    @staticmethod
    def extract_volume_from_text(text: str) -> Optional[int]:
        import re
        m = re.search(r"(\d+)[ ]?mL", text, re.IGNORECASE)
        if m:
            return int(m.group(1))
        return None

    @staticmethod
    def classify_category_from_text(text: str) -> Optional[str]:
        text = text.lower()
        categories = ['vodka','rum','tequila','liqueur','curacao','bitters','syrup','gin','whiskey']
        for cat in categories:
            if cat in text:
                return cat
        return None
