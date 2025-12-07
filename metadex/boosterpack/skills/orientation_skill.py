class OrientationSkill:
    """Skill: Provide high-level orientation about the StashKit/Barback architecture
    using the MetaDex as the backing ontology."""

    skill_id = "stashkit.dev.orientation"

    def __init__(self, metadex: dict):
        self.metadex = metadex

    def describe_entity(self, entity_id: str) -> dict:
        return self.metadex.get("entities", {}).get(entity_id, {})

    def describe_api(self, entity_id: str) -> dict:
        ent = self.metadex.get("entities", {}).get(entity_id, {})
        return ent.get("api", {})
