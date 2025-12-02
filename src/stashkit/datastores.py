from abc import ABC, abstractmethod
from typing import Dict, Type, Any
import json

class Datastore(ABC):
    _registry: Dict[str, Type['Datastore']] = {}

    def __init_subclass__(cls, datastore_name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._registry[datastore_name] = cls

    @classmethod
    def get(cls, name: str) -> Type['Datastore']:
        if name not in cls._registry:
            raise ValueError(f"Datastore {name} not registered")
        return cls._registry[name]

    @abstractmethod
    def save(self, stash) -> Any:
        pass

    @abstractmethod
    def load(self) -> list:
        pass

class JSONDatastore(Datastore, datastore_name="json"):
    def save(self, stash):
        data = [item.model_dump() for item in stash.list()]
        with open("stash.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return "stash.json"

    def load(self):
        with open("stash.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
