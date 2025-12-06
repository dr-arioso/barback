
# Integration for Services / Daemon Processes

StashKit can be embedded in:

- background processing daemons
- photo watcher services
- POS integrations
- mobile/desktop sync services

## File watcher example

```
while True:
    for image in watch_folder():
        result = pipeline.run(image)
        stash.add(result.model)
    stash.save()
    sleep(2)
```

Daemon guidelines:

- Use SQLite for long‑running, concurrent writes  
- Use journaling if power outages are possible  
- Log structured provenance events  
- Run pipelines in worker threads or queues  
