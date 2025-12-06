
# Runtime Integration Flow Examples

## Example 1: UPC Scan
1. UPCScanSkill extracts code
2. UPCLookupSkill retrieves brand + product_name
3. ClassificationEngine maps features → taxonomy path
4. StashTags inferred from BoozeDex overlays
5. Entry written to stash

## Example 2: Image-Only Bottle
1. AIVisionSkill produces descriptors
2. OCRSkill extracts ABV + volume
3. ClassificationEngine determines likely spirits category
4. Resolver loopback triggers UPCLookup if UPC is found
5. Confidence assigned, conflicts logged

## Example 3: Manual Entry
1. User enters name "Aperol"
2. ClassificationEngine finds `spirits.liqueurs.herbal.aperitivo.aperol_style`
3. Tags inferred automatically (bitter, citrus, aperitif)
