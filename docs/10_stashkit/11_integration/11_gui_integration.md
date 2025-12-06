
# Integration with GUI Frameworks

StashKit can be embedded into GUI workflows such as:

- Tkinter
- PySide6 / Qt for Python
- Kivy
- DearPyGUI
- Custom web UIs via backend APIs

## Tkinter Example

```
def on_photo_selected(file_path):
    result = pipeline.run(file_path)
    model = result.model
    name_var.set(model.product_name)
    abv_var.set(model.abv_percent)
```

GUI best practices:

- Offload pipeline execution to background threads  
- Never block the UI event loop  
- Reflect provenance and conflict markers in a friendly way  
- Use classification data to populate hierarchical dropdowns (e.g., BoozeDex selectors)  
