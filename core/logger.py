# core/logger.py
import logging
from pathlib import Path

LOG_FILE = Path("logs/runtime.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


def get_logger(name: str = __name__):
    return logging.getLogger(name)


def flush_logs(keep_fatal: bool = True):
    if not LOG_FILE.exists():
        return
    if keep_fatal:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        fatal = [L for L in lines if "ERROR" in L or "CRITICAL" in L]
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.writelines(fatal)
    else:
        try:
            LOG_FILE.unlink()
        except Exception:
            pass
