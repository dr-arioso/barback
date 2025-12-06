
# Local API Endpoints (UI Support)

The UI interacts with Barback through a lightweight HTTP or IPC API.

### `/scan`
POST image → returns classified result

### `/upc`
POST UPC → returns lookup result

### `/manual`
POST data → classification + storage

### `/search`
GET w/ filters → inventory list

### `/bottle/<id>`
GET → full record  
PUT → update  
DELETE → remove

These endpoints allow any UI (desktop or mobile) to integrate cleanly.
