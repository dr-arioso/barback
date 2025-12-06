
# Confidence Scoring

Every Skill must produce a `confidence` float between 0.0 and 1.0.

## Suggested Guidelines
- 1.0 = deterministic output (e.g., checksum)
- 0.8–1.0 = high certainty (ML with strong signal)
- 0.5–0.8 = medium certainty
- <0.5 = weak inference; Resolver should fallback

Confidence is not standardized across skills but must be consistent *within* each skill.
