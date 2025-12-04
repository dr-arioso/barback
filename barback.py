from __future__ import annotations
import argparse
import logging

from barback.core.pipeline import run_pipeline
from barback.resolvers import BottleResolver, GoogleVisionResolver, OpenAIVisionResolver

def main() -> None:
    parser = argparse.ArgumentParser(description="Barback - home bar inventory helper")
    parser.add_argument("--folder", required=True, help="Folder containing bottle images")
    parser.add_argument(
        "--resolver",
        choices=["bottle", "google", "openai"],
        default="bottle",
        help="Resolver to use for the AI Vision stage",
    )
    parser.add_argument(
        "--no-manual",
        action="store_true",
        help="Disable manual completion (for batch/quiet runs)",
    )
    args = parser.parse_args()

    if args.resolver == "google":
        resolver = GoogleVisionResolver()
    elif args.resolver == "openai":
        resolver = OpenAIVisionResolver()
    else:
        resolver = BottleResolver()

    stash = run_pipeline(
        folder=args.folder,
        resolver=resolver,
        allow_manual=not args.no_manual,
    )

    print("\nFinal BottleStash:")
    for bottle in stash:
        print(f"- {bottle.name or 'Unknown'} ({bottle.brand}) [{bottle.category}]")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
