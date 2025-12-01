# core/file_manager.py
from pathlib import Path
import shutil
from typing import List, Dict

BASE_DATA_DIR = Path("data")
INPUT_FOLDER = BASE_DATA_DIR / "input_photos"
RESOLVED_FOLDER = BASE_DATA_DIR / "resolved_photos"
UNRESOLVED_FOLDER = BASE_DATA_DIR / "unresolved_photos"


def setup_default_folders(base_dir: Path = BASE_DATA_DIR) -> Dict[str, Path]:
    for folder in (INPUT_FOLDER, RESOLVED_FOLDER, UNRESOLVED_FOLDER):
        folder.mkdir(parents=True, exist_ok=True)
    return {"input": INPUT_FOLDER, "resolved": RESOLVED_FOLDER, "unresolved": UNRESOLVED_FOLDER}


def get_photo_files(folder: Path) -> List[Path]:
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    files = sorted(folder.glob("*.jpg")) + sorted(folder.glob("*.jpeg")) + sorted(folder.glob("*.png"))
    return files


def move_photo(src_path: Path, dest_folder: Path, brand: str = None, volume_ml: int = None) -> Path:
    src_path = Path(src_path)
    dest_folder = Path(dest_folder)
    dest_folder.mkdir(parents=True, exist_ok=True)
    ext = src_path.suffix
    name_base = "unidentified"
    if brand:
        safe_brand = "".join(c for c in brand if c.isalnum() or c in (" ", "-", "_")).strip().replace(" ", "_")
        name_base = safe_brand
    if volume_ml:
        name_base = f"{name_base}_{volume_ml}ml"
    dest = dest_folder / f"{name_base}{ext}"
    counter = 1
    while dest.exists():
        dest = dest_folder / f"{name_base}_{counter}{ext}"
        counter += 1
    shutil.move(str(src_path), str(dest))
    return dest
