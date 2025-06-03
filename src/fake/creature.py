from src.model.creature import Creature

_creatures = [
    Creature(name="yeti", country="CN", area="Hymalayas", description="Hirsute Himalayan", aka="Abominable Snowman"),
    Creature(name="Bigfoot", description="Yeti's Cousin Eddie", country="US", area="*", aka="Sasquatch"),
]

def get_all() -> list[Creature]:
    return _creatures

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    return creature

def modify(creature: Creature) -> Creature:
    return creature

def replace(creature: Creature) -> Creature:
    return creature

def delete(creature: Creature) -> Creature:
    return creature

