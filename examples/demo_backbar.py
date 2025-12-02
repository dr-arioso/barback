from barback.models import Bottle
from barback.backbar import BackBar

def main():
    # Create a BackBar stash
    bar = BackBar(resolver_name="upc")

    # Add some bottles
    bottle1 = Bottle(
        canonical_name="Bombay Sapphire Gin",
        aliases=["Bombay Gin"],
        categories=["Gin", "Spirit"],
        brand="Bombay",
        height_mm=300,
        width_mm=70,
        depth_mm=70,
        labeled_volume_ml=750,
    )

    bottle2 = Bottle(
        canonical_name="Angostura Aromatic Bitters",
        aliases=["Angostura Bitters"],
        categories=["Bitters", "Flavoring"],
        brand="Angostura",
        height_mm=150,
        width_mm=40,
        depth_mm=40,
        labeled_volume_ml=200,
    )

    # Add to BackBar
    bar.add(bottle1)
    bar.add(bottle2)

    # Iterate through bottles
    print("Current bottles in BackBar:")
    for b in bar:
        print(f"- {b.canonical_name} ({b.labeled_volume_ml} ml)")

    # Total volume
    print(f"Total volume: {bar.total_volume()} ml")

    # Resolve UPCs (stub, does nothing yet)
    for b in bar:
        b.resolve_upc()
        print(f"{b.canonical_name} UPC: {b.upc}")

    # Export stash to JSON
    output_file = bar.output("json")
    print(f"BackBar exported to {output_file}")

if __name__ == "__main__":
    main()
