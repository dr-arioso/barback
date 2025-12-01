
from pathlib import Path
from backends import BottleResolver
from core.pipeline import run_pipeline

# Dynamic resolver map
resolver_classes = {}

def run_gui_identification(folder_path: str, resolver_name: str = None, silent: bool = False):
    folder = Path(folder_path)
    if resolver_name and resolver_name in resolver_classes:
        resolver_obj = resolver_classes[resolver_name]()
    else:
        resolver_obj = BottleResolver()
    results = run_pipeline(folder, resolver_obj=resolver_obj, silent=silent)
    return results
