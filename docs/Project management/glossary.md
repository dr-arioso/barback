# Glossary

**Resolver** – Module converting input into structured Item/Product data.

**ProductResolver** – Abstract base class for home-bar product resolvers (CLI/TUI/GUI pipelines may use this).

**Output Plugin** – Module exporting results into a specific format.

**Item** – Generic representation of a product.

**Product** – Item subclass with product-specific fields (brand, UPC, dimensions).

**Stash** – Container for Items or Products.

**StashKit** – Embedded library providing resolvers, output plugins, Items, and Stash management.

**Barback** – Home-bar management project that implements StashKit and provides user-facing interfaces (CLI/TUI/GUI).
