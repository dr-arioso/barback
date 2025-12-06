
# Integration with Web Applications

StashKit can serve as the backend for a web application using:

- FastAPI
- Flask
- Django
- Quart
- Starlette

## Example FastAPI integration

```
from fastapi import FastAPI, UploadFile
from stashkit.pipelines import Pipeline
from stashkit.resolvers import BottleResolver

app = FastAPI()
pipeline = Pipeline(resolvers=[BottleResolver()])

@app.post("/scan")
async def scan_bottle(file: UploadFile):
    path = "/tmp/" + file.filename
    with open(path, "wb") as f:
        f.write(await file.read())
    result = pipeline.run(path)
    return result.model.dict()
```

This pattern enables Barback‑style bottle scanning in any web client (React, Svelte, Flutter Web).
