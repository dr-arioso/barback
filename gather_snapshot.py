import os
import zipfile
from pathlib import Path

# Path to the root of your project
PROJECT_ROOT = Path(__file__).parent
DOCS_DIR = PROJECT_ROOT / "docs"
OUTPUT_ZIP = PROJECT_ROOT / "barback_project_snapshot.zip"

# Files to always include at the root of the project
ROOT_FILES = ["README.md", "CHANGELOG.md"]

# Optional: add config files or environment files
CONFIG_FILES = [".env", "config.yaml"]

def gather_project_snapshot():
    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add docs folder
        if DOCS_DIR.exists():
            for root, _, files in os.walk(DOCS_DIR):
                for file in files:
                    if file.endswith((".md", ".txt")):
                        file_path = Path(root) / file
                        zipf.write(file_path, file_path.relative_to(PROJECT_ROOT))
        else:
            print(f"Docs directory '{DOCS_DIR}' does not exist. Skipping docs.")

        # Add root files
        for fname in ROOT_FILES + CONFIG_FILES:
            file_path = PROJECT_ROOT / fname
            if file_path.exists():
                zipf.write(file_path, file_path.name)

    print(f"Project snapshot zipped successfully into '{OUTPUT_ZIP}'.")

if __name__ == "__main__":
    gather_project_snapshot()
