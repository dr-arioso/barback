
# Error Design Principles

## 1. Structured Messages
Each error includes:
- human-readable message  
- machine-parsable details  
- optional resolution hints  

## 2. Context Embedding
Errors capture:
- originating module  
- skill/resolver/pipeline name  
- input parameters (masked for safety)  
- original exception (if any)  

## 3. Safe Defaults
Errors never expose:
- API keys  
- sensitive metadata  
- raw user-provided data without sanitation  

## 4. Re-Throw Strategy
Subsytems may wrap lower-level errors:

```
try:
    result = skill.execute(data)
except Exception as e:
    raise SkillExecutionError("Vision skill failed", cause=e)
```
