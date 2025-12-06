
# Image Helpers

Used by VisionSkill, OCRSkill, UPCSkill, and pipelines.

Provides:
- EXIF extraction
- orientation correction
- resizing, cropping
- image hashing for caching
- safe tempfile management

Example:

```
from stashkit.helpers.image import normalize_image

path = normalize_image("raw_photo.jpg")
```
