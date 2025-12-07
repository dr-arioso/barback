class ArchitectureResolver:
    """Resolver: Answer questions about StashKit and Barback using the MetaDex."""

    resolver_id = "stashkit.dev.architecture"

    def __init__(self, metadex: dict):
        self.metadex = metadex

    def get_entity(self, entity_id: str) -> dict:
        return self.metadex.get("entities", {}).get(entity_id, {})

    def list_related(self, entity_id: str) -> dict:
        relationships = self.metadex.get("relationships", [])
        related = [r for r in relationships if r.get("from") == entity_id]
        return {"entity": entity_id, "related": related}
