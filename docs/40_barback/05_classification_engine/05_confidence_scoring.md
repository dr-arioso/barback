
# Confidence Scoring

Confidence is derived from multiple weighted factors:

- taxonomy match strength  
- number of supported features  
- cross-source agreement  
- brand database lookups  
- UPC reliability  
- resolver consensus  

### Formula (conceptual)
```
confidence = 
  (0.35 * direct_match_score) +
  (0.20 * feature_support_score) +
  (0.25 * source_reliability_score) +
  (0.20 * consensus_score)
```
Scores normalize to 0–1.
