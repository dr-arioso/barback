# core/result_writer.py
import csv
import json
from pathlib import Path
from typing import List, Dict, Any
from core.errors import PipelineError, FileError

try:
    import openpyxl
except Exception:
    openpyxl = None

OUT_DIR = Path(".")

DEFAULT_CSV = "bar_inventory.csv"
DEFAULT_JSON = "bar_inventory.json"
DEFAULT_XLSX = "bar_inventory.xlsx"


def write_results(results: List[Dict[str, Any]], output_format: str = "csv", output_file: str = None):
    output_format = (output_format or "csv").lower()
    if output_format == "csv":
        out = Path(output_file or DEFAULT_CSV)
        if results:
            keys = sorted({k for r in results for k in r.keys()})
        else:
            keys = []
        with out.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for r in results:
                writer.writerow(r)
        return str(out)
    elif output_format == "json":
        out = Path(output_file or DEFAULT_JSON)
        with out.open("w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        return str(out)
    elif output_format == "xlsx":
        out = Path(output_file or DEFAULT_XLSX)
        if openpyxl is None:
            raise RuntimeError("openpyxl is required for xlsx output")
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        if results:
            keys = sorted({k for r in results for k in r.keys()})
        else:
            keys = []
        ws.append(keys)
        for r in results:
            ws.append([r.get(k) for k in keys])
        wb.save(out)
        return str(out)
    else:
        raise ValueError("Unsupported output format")
