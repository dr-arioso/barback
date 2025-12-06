
# Text Helpers

Text utilities used by Skills and Resolvers.

Includes:
- normalization (unicode, whitespace, punctuation)
- fuzzy matching
- string similarity scoring
- safe substring search
- tokenization utilities

Example:

```
from stashkit.helpers.text import normalize

clean = normalize(" CÔINTREAU   ")
# → "cointreau"
```
