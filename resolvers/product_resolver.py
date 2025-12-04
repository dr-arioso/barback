from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import logging
import requests

logger = logging.getLogger(__name__)

class ProductResolver(ABC):
    """Abstract base class for all product resolvers."""

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
