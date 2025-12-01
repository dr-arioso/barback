# tools/check_project.py
import importlib, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

modules = [
    "core.file_manager", "core.pipeline", "core.brand_matching", "core.result_writer",
    "backends.base_backend", "backends.simple_backend", "interface.cli", "interface.gui", "config.config"
]

for m in modules:
    try:
        importlib.import_module(m)
        print("OK:", m)
    except Exception as e:
        print("ERR:", m, e)
