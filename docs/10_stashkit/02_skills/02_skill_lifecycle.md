
# Skill Lifecycle

1. **Initialization**  
   The Skill loads configuration, API keys, or resources.

2. **Execution**  
   The `execute(input)` method runs the atomic inference.

3. **Validation**  
   Skill output is validated against a standard schema.

4. **Return**  
   A dictionary containing:
   - `result`
   - `confidence`
   - `metadata`

5. **Error Handling**  
   Skills must raise structured SkillError exceptions on failure.

Skills must be deterministic on identical inputs unless explicitly marked otherwise.
