
# Template: Persistence Backend (Optional)

A Booster Pack may include SQL or JSON schema templates:

### Example SQLite schema

```
CREATE TABLE bottles (
  id TEXT PRIMARY KEY,
  brand TEXT,
  product_name TEXT,
  classification TEXT,
  volume_ml INTEGER,
  abv REAL,
  metadata TEXT
);
```
