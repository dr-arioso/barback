
# BoozeDex Standard Field Definitions

These fields represent the **canonical attributes** shared across all beverage products.

### Core Fields  
- **brand**: string  
- **product_name**: string  
- **classification**: DexTree path  
- **abv_percent**: float (0–100)  
- **labeled_volume_ml**: integer  
- **country_of_origin**: optional string  
- **ingredients**: optional list  
- **aliases**: optional list  
- **sku**: optional string  

### Metadata Fields  
- **tasting_notes**: optional structured list  
- **flavor_profile_tags**: list of StashTags  
- **cocktail_roles**: list of StashTags  
- **production_methods**: optional list  

### Provenance Fields  
Added automatically by StashKit:  
- **confidence**  
- **resolver_log**  
- **skill_outputs**  
