# StashKit Models

Defines the core data structures used by StashKit.

## Item
Generic base class for products/items.
- `id: UUID`
- `canonical_name: str`
- `aliases: List[str]`
- `categories: List[str]` (must contain at least one)
- `photo: Optional[str]`
- `notes: Optional[str]`

## Product (subclass of Item)
Adds product-specific fields:
- `brand: str`
- `manufacturer: Optional[str]`
- `sku: Optional[str]`
- `upc: Optional[str]`
- `upc_photo: Optional[str]`
- Dimensions: `height_mm`, `width_mm`, `depth_mm`
- `weight_g: Optional[float]`

### Methods
- `resolve_upc(resolver_name: Optional[str])`  
  Attempts to resolve the UPC using the configured resolver pipeline:
  1. Default `UPCResolver`
  2. Optional named resolver
  3. Fallback to `ManualResolver`
