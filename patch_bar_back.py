# patch_cli_silent_flag.py
from pathlib import Path
import argparse
import logging
from core.pipeline import run_pipeline
from backends.simple_backend import SimpleBackend  # or ProductResolver/BottleResolver if renamed

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Process product images")
    parser.add_argument("folder", type=str, help="Folder containing images")
    parser.add_argument("--backend", type=str, default=None, help="Resolver/backend to use")
    parser.add_argument("--silent", action="store_true", help="Suppress interactive prompts")
    args = parser.parse_args()

    # Instantiate the resolver/backend
    resolver = SimpleBackend()  # or dynamically select if backend option is provided

    # Pass silent flag to run_pipeline
    results = run_pipeline(args.folder, resolver_obj=resolver, silent=args.silent)

    for r in results:
        print(r)

if __name__ == "__main__":
    main()
 