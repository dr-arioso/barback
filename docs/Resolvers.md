# Resolver Architecture

Resolvers translate raw image files into structured product metadata.

Each resolver:
- Inherits from `ResolverBase`
- Returns a dict containing at minimum:
  - `product_id`
  - `barcode`
  - `title`
  - `confidence`
  - `raw` (full provider response)

## Required Keys
```json
{
  "product_id": "...",
  "barcode": "...",
  "title": "...",
  "confidence": 0.94,
  "raw": {}
}
```

## Planned Resolvers
- **OpenAIVisionResolver**
- **GoogleVisionResolver**
- **BarcodeOnlyResolver**
- **CachedResolver** (store + reuse API responses)
- **FallbackResolver** (try multiple backends automatically)
