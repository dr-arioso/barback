# Output Plugins

Output plugins format the normalized results into one or more structured files.

## Current Targets
- **JSON** – always supported
- **CSV** – for spreadsheets
- **HTML (future)** – table with inline images

## Example Interface
```python
class JSONOutput(OutputBase):
    name = "json"
    file_extension = ".json"

    def generate(self, results, output_dir):
        ...
```
