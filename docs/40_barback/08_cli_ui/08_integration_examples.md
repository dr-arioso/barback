
# Integration Examples

## Example 1: Python Script Using Local API
```
import requests
resp = requests.post("http://localhost:5000/scan", files={"image": open("bottle.jpg","rb")})
print(resp.json())
```

## Example 2: Node.js UI Integration
```
const result = await fetch("/scan", {
  method: "POST",
  body: formData
}).then(r => r.json());
```

## Example 3: Command-Line Alias
```
alias scanb='barback scan "$1"'
scanb ~/Pictures/tequila.png
```

These examples illustrate how Barback’s core remains interface-agnostic.
