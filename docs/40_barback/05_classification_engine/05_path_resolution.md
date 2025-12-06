
# Taxonomy Path Resolution

The engine maps extracted features to valid BoozeDex taxonomy paths.

### Direct Match
Input: "bourbon"  
→ `spirits.whiskey.bourbon`

### Nested Match
Input: "reposado"  
→ `spirits.agave.tequila.reposado`

### Conflict Example
Input: "orange liqueur"  
Candidates:
- `spirits.liqueurs.fruit.orange.triple_sec`
- `spirits.liqueurs.fruit.orange.curacao`

Resolution uses:
- flavor hints
- brand lookup (if available)
- regional indicators
