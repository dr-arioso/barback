
# CLI Commands

Barback exposes a modular, scriptable command-line interface.

## `barback scan <image>`
Runs the full pipeline using AIVision + OCR + classification.
```
barback scan bottle.jpg
```

## `barback upc <code>`
Runs UPCScanSkill and UPCLookupSkill.
```
barback upc 085000029503
```

## `barback add`
Performs guided manual entry with classification assist.
```
barback add --name "Aperol"
```

## `barback search`
Search inventory.
```
barback search --tag bitter --abv-max 40
```

## `barback show <id>`
Display a stored bottle with tags, provenance, notes.

## `barback edit <id>`
Modify or annotate stored entries.

## `barback export`
Export the stash to JSON, CSV, or SQL.
