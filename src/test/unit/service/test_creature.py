from src.model.creature import Creature
from src.service import creature as code

sample = Creature(name="yeti", country="CN", area="Hymalayas", description="Hirsute Himalayan", aka="Abominable Snowman")

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one("yeti")
    assert resp == sample

def test_get_missing():
    resp = code.get_one("boxturtle")
    assert resp is None

