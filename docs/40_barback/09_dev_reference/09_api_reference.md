
# Barback API Reference

## Core Entry Points

### `barback.scan(image_path)`
Runs full bottle classification pipeline.

### `barback.upc(code)`
Runs UPC-only lookup flow.

### `barback.add_manual(fields)`
Manual entry with classification assist.

### `barback.search(filters)`
Search persistent stash using taxonomy, tags, or metadata.

### `barback.get(id)`
Retrieve detailed bottle record.

### `barback.update(id, data)`
Update an existing record.

### `barback.export(fmt)`
Export inventory.

All functions return structured models compliant with BoozeDex schema.
