from typing import Optional, List, Dict
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def get_photo_files(folder: Path) -> List[Path]:
    return [p for p in folder.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]


from resolvers import BottleResolver


from backends import ProductResolver as BottleResolver


from backends.simple_backend import BottleResolver
from typing import Optional, List, Dict, Any
from pathlib import Path


from pathlib import Path
from backends.simple_backend import SimpleBackend as BottleResolver


from pathlib import Path
import logging
from backends import BottleResolver

logger = logging.getLogger(__name__)

def run_pipeline(folder: str, resolver_obj=None, silent=False):
    """
    Run product identification on all images in folder.
    resolver_obj: instance of ProductResolver (default: BottleResolver)
    silent: if True, suppress interactive prompts and TUI dialogs
    """
    if resolver_obj is None:
        resolver_obj = BottleResolver()

    folder_path = Path(folder)
    results = []

    for img_file in folder_path.glob("*.jpg"):
        res_primary = resolver_obj.identify_from_image(str(img_file))
        res_final = res_primary.copy()
        missing_fields = [k for k in ("brand", "volume_ml", "dimensions_cm") if not res_primary.get(k)]

        # Failover to BottleResolver for missing data
        if missing_fields and not isinstance(resolver_obj, BottleResolver):
            fallback = BottleResolver()
            res_fallback = fallback.identify_from_image(str(img_file))
            for key in missing_fields:
                res_final[key] = res_fallback.get(key, None)
            logger.info(f"{img_file.name}: supplemented missing fields from BottleResolver: {missing_fields}")

        # Check for conflicting fields
        conflicts = {k: (res_primary.get(k), res_fallback.get(k))
                     for k in ("brand", "volume_ml", "dimensions_cm")
                     if 'res_fallback' in locals() and
                     res_primary.get(k) and res_fallback.get(k) and
                     res_primary.get(k) != res_fallback.get(k)}

        if conflicts:
            for field, (val_primary, val_fallback) in conflicts.items():
                if silent:
                    logger.error(f"{img_file.name}: conflict in '{field}' (primary='{val_primary}' vs fallback='{val_fallback}'). Cannot resolve in silent mode.")
                    raise SystemExit(1)
                else:
                    choice = None
                    while choice not in ('1', '2'):
                        print(f"Conflict in '{field}' for {img_file.name}:")
                        print(f"1) Primary: {val_primary}")
                        print(f"2) Fallback: {val_fallback}")
                        choice = input("Choose value [1/2]: ").strip()
                    res_final[field] = val_primary if choice == '1' else val_fallback
                    logger.info(f"{img_file.name}: user selected {res_final[field]} for '{field}'")

        results.append(res_final)

    return results
