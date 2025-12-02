import os

# -------------------------------
# Directory structure
# -------------------------------
dirs = [
    "src/stashkit",
    "barback",
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

# -------------------------------
# Files and their contents
# -------------------------------
files = {
    "pyproject.toml": """[build-system]
requires = ["setuptools", "wheel", "pydantic>=2.0"]
build-backend = "setuptools.build_meta"

[project]
name = "barback"
version = "0.0.1"
description = "Barback + StashKit (development package)"
readme = "README.md"
requires-python = ">=3.9"

[tool.setuptools.packages.find]
where = ["src"]
""",
    "src/stashkit/__init__.py": """\"\"\"StashKit — core data & storage utilities for barback.\"\"\"

from .models import Item, Product
from .stash import Stash
from .datastores import Datastore
from .resolvers import Resolver
""",
    "src/stashkit/models.py": """from __future__ import annotations
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional
from uuid import uuid4, UUID

class Item(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    canonical_name: str
    aliases: List[str] = Field(default_factory=list)
    categories: List[str] = Field(default_factory=list)
    photo: Optional[str] = None
    notes: Optional[str] = None

    @model_validator(mode='before')
    def ensure_categories(cls, values):
        cats = values.get('categories')
        if not cats or len(cats) == 0:
            raise ValueError("Item must have at least one category")
        return values

class Product(Item):
    brand: str
    manufacturer: Optional[str] = None

    sku: Optional[str] = None
    upc: Optional[str] = None
    upc_photo: Optional[str] = None

    height_mm: float
    width_mm: float
    depth_mm: float
    weight_g: Optional[float] = None

    def resolve_upc(self, resolver_name: Optional[str] = None):
        from .resolvers import Resolver
        upc_resolver_cls = Resolver.get("upc")
        upc_resolver = upc_resolver_cls()
        upc_result = None
        if self.photo:
            upc_result = upc_resolver.resolve(self.photo)
        if not upc_result and resolver_name:
            next_resolver_cls = Resolver.get(resolver_name)
            next_resolver = next_resolver_cls()
            upc_result = next_resolver.resolve(self.photo)
        if not upc_result:
            manual_cls = Resolver.get("manual")
            manual_resolver = manual_cls()
            upc_result = manual_resolver.resolve(self.photo)
        self.upc = upc_result
        return self.upc
""",
    "src/stashkit/stash.py": """from __future__ import annotations
from typing import Generic, TypeVar, Dict, List, Optional
from .models import Item
from .datastores import Datastore
from .resolvers import Resolver

T = TypeVar("T", bound=Item)

class Stash(Generic[T]):
    def __init__(self, resolver_name: Optional[str] = None):
        self._items: Dict[str, T] = {}
        self.resolver_name = resolver_name

    def add(self, item: T):
        if item.id.hex in self._items:
            raise ValueError(f"Duplicate ID {item.id}")
        self._items[item.id.hex] = item

    def get(self, id: str) -> T:
        return self._items[id]

    def list(self) -> List[T]:
        return list(self._items.values())

    def find(self, **query) -> List[T]:
        results = []
        for item in self._items.values():
            if all(getattr(item, k, None) == v for k, v in query.items()):
                results.append(item)
        return results

    def __iter__(self):
        return iter(self._items.values())

    def output(self, datastore_name: str):
        store_cls = Datastore.get(datastore_name)
        store = store_cls()
        return store.save(self)

    def resolve_item(self, input_data):
        if not self.resolver_name:
            raise RuntimeError("No resolver configured")
        resolver_cls = Resolver.get(self.resolver_name)
        resolver = resolver_cls()
        return resolver.resolve(input_data)
""",
    "src/stashkit/datastores.py": """from abc import ABC, abstractmethod
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
""",
    "src/stashkit/resolvers.py": """from abc import ABC, abstractmethod
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
""",
    "barback/models.py": """from stashkit.models import Product

class Bottle(Product):
    labeled_volume_ml: int
    distiller: str
    bottler: str

    @property
    def manufacturer(self):
        return self.distiller or self.bottler or super().manufacturer
""",
    "barback/backbar.py": """from stashkit.stash import Stash
from .models import Bottle

class BackBar(Stash[Bottle]):
    \"\"\"Domain-specific stash for bottles\"\"\"

    def total_volume(self) -> float:
        return sum(b.labeled_volume_ml for b in self)
""",
}

# -------------------------------
# Write files
# -------------------------------
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("StashKit scaffolding created successfully. You can now:")
print("1. git add src/stashkit barback pyproject.toml")
print("2. git commit -m 'Add StashKit and BackBar scaffolding'")
print("3. pip install -e .")
