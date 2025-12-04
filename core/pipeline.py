from __future__ import annotations
from pathlib import Path
from typing import Iterable
import logging

from barback.models import Bottle
from barback.inventory.bottle_stash import BottleStash
from stashkit.resolvers.base import BaseResolver

logger = logging.getLogger(__name__)

def iter_image_files(folder: Path) -> Iterable[Path]:
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        yield from folder.glob(ext)

def run_pipeline(
    folder: str,
    resolver: BaseResolver[Bottle],
    allow_manual: bool = True,
) -> BottleStash:
    folder_path = Path(folder)
    if not folder_path.is_dir():
        raise ValueError(f"{folder} is not a directory")

    stash = BottleStash()

    for image_path in iter_image_files(folder_path):
        logger.info(f"Resolving bottle from image {image_path.name}")
        bottle = resolver.resolve(image_path=str(image_path), allow_manual=allow_manual)
        stash.add(bottle)
        logger.info(f"Resolved: {bottle.name or 'Unknown'} ({bottle.brand})")

    return stash
