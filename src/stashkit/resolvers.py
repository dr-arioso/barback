from abc import ABC, abstractmethod
from typing import Dict, Type, Any

class Resolver(ABC):
    _registry: Dict[str, Type['Resolver']] = {}

    def __init_subclass__(cls, resolver_name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._registry[resolver_name] = cls

    @classmethod
    def get(cls, name: str) -> Type['Resolver']:
        if name not in cls._registry:
            raise ValueError(f"Resolver {name} not registered")
        return cls._registry[name]

    @abstractmethod
    def resolve(self, input_data) -> Any:
        pass

class UPCResolver(Resolver, resolver_name="upc"):
    def resolve(self, input_data):
        return None  # placeholder

class ManualResolver(Resolver, resolver_name="manual"):
    def resolve(self, input_data):
        return None  # placeholder
