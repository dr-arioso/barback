from __future__ import annotations
from typing import Dict, Any, Iterable, Optional
from abc import ABC, abstractmethod

class ManualResolver(ABC):
    """
    UI-agnostic manual completion of missing fields.
    A Barback CLI or GUI can implement this using stdin/Qt/etc.
    """

    @abstractmethod
    def list_known_values(self, field: str) -> Iterable[str]:
        """Return known values for a field (e.g. brands, categories)."""
        raise NotImplementedError

    @abstractmethod
    def prompt(self, field: str, current: Optional[str],
               candidates: Iterable[str]) -> str:
        """Ask the user (or UI) for a definitive value."""
        raise NotImplementedError

    @abstractmethod
    def fill_missing(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Given partial fields, fill in missing/invalid values."""
        raise NotImplementedError
