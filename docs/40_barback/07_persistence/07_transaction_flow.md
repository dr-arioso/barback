
# Persistence Transaction Flow

1. Classification result produced  
2. Resolver packages final model  
3. Backend validates model (schema + constraints)  
4. Write operation:
   - insert new record OR
   - update existing record (if merging)
5. Backend returns:
   - updated model
   - confirmation status
   - conflict warnings (if merging)

All operations are atomic.
