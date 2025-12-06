
# BoozeDex Schema Constraints

### ABV Rules  
- Beer: 0–20%  
- Wine: 0–45% (includes fortified)  
- Spirits: 20–90%  
- Liqueurs: 10–60%  
- Mixers/non-alcoholic: 0–5%  

### Volume Rules  
- Must be positive integer  
- Maximum reasonable bound: 10,000 ml  

### Taxonomy Constraints  
- Classification path must resolve to a DexNode  
- Classification must be unique among siblings  
- Certain nodes impose field requirements:  
  - Mezcal must include agave variety  
  - Vermouth must include wine base  

These enforce domain correctness without being overly restrictive.
