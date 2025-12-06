
# Models Subsystem Overview

The **Models subsystem** defines structured, typed domain objects used throughout
StashKit and applications like Barback. Models represent the final validated
output of pipelines and resolvers. They are:

- Strictly typed (Pydantic or Python dataclasses)
- Validation-enforced
- Serializable
- Compatible with Stashes
- Indexed via taxonomy and metadata

Models form the backbone of structured data integrity within the StashKit ecosystem.
