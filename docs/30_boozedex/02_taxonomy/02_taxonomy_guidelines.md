
# Taxonomy Authoring Guidelines

### 1. Paths must be unique  
No two nodes may share the same full path.

### 2. Names must be stable  
Changing node identifiers breaks downstream models—prefer adding aliases instead.

### 3. Polyhierarchy is handled by tags  
Taxonomy is strictly hierarchical; functional roles belong in StashTags.

### 4. Children inherit constraints  
Example:  
- All whiskey is a spirit  
- All bourbon is a whiskey  
- All tequila is agave-based

### 5. Nodes should be intuitive for non-experts  
E.g., Users think “gin,” not “juniper-flavored neutral spirit.”

### 6. Do not include brands in taxonomy  
Brands belong in models, not in DexTrees.
