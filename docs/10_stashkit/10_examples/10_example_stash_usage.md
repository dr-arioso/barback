
# Example: Using a Stash

```
from stashkit.stashes import BottleStash
stash = BottleStash()

stash.add(bottle_model)
found = stash.find(upc="012345678905")
print(found)
```

You can also export/import:

```
stash.save()
stash2 = BottleStash()
stash2.load()
```
