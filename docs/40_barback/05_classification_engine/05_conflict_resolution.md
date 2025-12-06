
# Conflict Resolution

Conflicts occur when multiple candidates receive similar scores.

### Strategies
- **Confidence-weighted** (default)
- **High-trust-source override** (UPC > AI > OCR)
- **User confirmation** if scores fall within narrow range
- **Loopback classification** if new data emerges (e.g., ABV discovered)

### Example
Input: "orange liqueur"

Candidates:
- triple_sec (0.68)
- curacao (0.64)

Engine chooses triple_sec but logs ambiguity:
```
"provenance": {
  "alternates": ["curacao"],
  "conflict_level": "medium"
}
```
