
# Resolver Design Patterns

## 1. Ordered Skill Chains
Resolvers execute skills in a predefined order:
- high-probability skills first
- then fallback skills
- then manual entry

## 2. Conditional Skills
Resolvers may modify the chain based on partial results.

Example:
- No UPC found → skip UPC lookup
- VisionSkill discovers UPC → restart Skill chain

## 3. Loopback Pattern
Resolvers may restart from the top when new key information is discovered.
This prevents premature resolution.

## 4. Confidence-Aware Merging
When multiple skills return the same field:
- highest confidence wins
- close values trigger “needs review”
- contradictions raise conflict warnings

