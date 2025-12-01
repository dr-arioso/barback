
import argparse
from pathlib import Path
from backends import BottleResolver
from core.pipeline import run_pipeline

# Dynamic resolver map
resolver_classes = {}

def main():
    parser = argparse.ArgumentParser(description="Identify products in a folder of images")
    parser.add_argument("folder", type=str, help="Path to folder with images")
    parser.add_argument("--resolver", type=str, default=None, help="Resolver class name to use")
    parser.add_argument("--silent", action="store_true", help="Suppress interactive prompts")
    args = parser.parse_args()

    folder = Path(args.folder)
    silent = args.silent

    if args.resolver and args.resolver in resolver_classes:
        resolver_obj = resolver_classes[args.resolver]()
    else:
        resolver_obj = BottleResolver()

    results = run_pipeline(folder, resolver_obj=resolver_obj, silent=silent)

    for r in results:
        print(r)

if __name__ == "__main__":
    main()
