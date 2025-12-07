```mermaid
flowchart TD
    A[Source YAML\ncore/ relationships/ rules/] --> B[Load YAML]
    B --> C[Normalize Values\n(lists, mappings, scalars)]
    C --> D[Validate Entities]
    C --> E[Build Relationship List]
    C --> F[Load Rules]
    F --> G[Apply Trait Propagation]
    D --> H[Derived Structures\n(reverse relationships, etc.)]
    E --> H
    G --> H
    H --> I[Assemble MetaDex JSON]
    I --> J[Write metadex.json\nwith version_info]
```
