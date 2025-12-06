
# Feature Extractors

Feature extractors convert messy text into structured indicators.

### Extracted Features
- category keywords (e.g., bourbon, rum, IPA)
- style terms (e.g., reposado, fernet, vermouth)
- flavor descriptors
- ABV numeric detection
- volume detection (e.g., 750ml, 1L)
- region hints (Kentucky, Oaxaca, Speyside)

### Example Extractor Output
```
{
  "keywords": ["bourbon"],
  "abv": 45,
  "volume_ml": 750,
  "region": "kentucky",
  "hints": ["oak", "vanilla"]
}
```

These feed into scoring and disambiguation.
