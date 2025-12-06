
# Error Schema

Standard StashKit error structure:

```
{
  "type": "SkillExecutionError",
  "message": "OCR failed to process image",
  "context": {
      "skill": "ocr_skill",
      "input_summary": "...",
      "latency_ms": 1034,
  },
  "cause": "TesseractError(... stack trace ...)",
  "hint": "Ensure image is upright and not blurred."
}
```

This structure is optimized for:
- debugging  
- provenance  
- UI display in consuming apps  
