from examples.model import Creature

_creatures: list[Creature] = [
    Creature(name="yeti", description="Hapless Himalayan", country="CN", area="Himalayas", aka="Abominable Snowman"),
    Creature(name="sasquatch", description="Yeti's Cousin Eddie", country="US", area="*", aka="Bigfoot")
]

def get_creatures() -> list[Creature]:
    return _creatures
