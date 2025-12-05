# API Reference (High-Level)

This is a human-written overview of the main public API surface. It is intended as a guide for developers and code-generation tools.

## StashKit

### Models

- `stashkit.models.Item`
  - Fields:
    - `id: UUID`
    - `name: str`
    - `description: Optional[str]`
    - `metadata: dict[str, Any]`
- `stashkit.models.Product(Item)`
  - Fields:
    - `upc: Optional[str]`
    - `brand: Optional[str]`
    - `manufacturer: Optional[str]`
    - `volume_ml: Optional[int]`

### Stash

- `stashkit.stash.Stash[T]`
  - Methods:
    - `add(item: T) -> None`
    - `__iter__() -> Iterable[T]`
    - `filter(predicate: Callable[[T], bool]) -> List[T]`

### Datastore

- `stashkit.datastore.StorageBackend[T]`
  - Methods:
    - `load() -> list[dict]`
    - `save(items: list[dict]) -> None`

### Resolvers

- `stashkit.resolvers.Skill`
  - `apply(fields: dict, input: dict) -> dict`
- `stashkit.resolvers.ProductResolver`
  - `__init__(model: Type[BaseModel], skills: list[Skill])`
  - `resolve(input: dict) -> BaseModel`

## Barback (example)

- `barback.models.Bottle(Product)`
  - Fields:
    - `abv: Optional[float]`
    - `category: Optional[str]`
    - `distiller: Optional[str]`
    - `height_mm: Optional[float]`, etc.
- `barback.resolvers.BottleResolver`
  - Wraps `ProductResolver` with `model=Bottle` and bottle-focused skills.
