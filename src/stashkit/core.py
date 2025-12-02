from dataclasses import dataclass
from typing import List

@dataclass
class Bottle:
    id: str
    name: str

class Collection:
    def __init__(self):
        self.items: List[Bottle] = []

    def add(self, bottle: Bottle):
        self.items.append(bottle)

    def __len__(self):
        return len(self.items)