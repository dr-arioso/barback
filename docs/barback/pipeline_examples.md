# Pipeline Examples

## Example 1: UPC-Based Bottle Identification
```python
input = {"upc": "088076163"}
bottle = bottle_resolver.resolve(input)
```

## Example 2: Vision-Based Bottle Identification
```python
input = {"image_path": "pictures/tequila.jpg"}
bottle = bottle_resolver.resolve(input)
```

## Example 3: Manual Fallback
```python
input = {"image_path": "blurry_image.jpg"}
bottle = resolver.resolve(input)
# Missing fields collected via manual prompt
```

