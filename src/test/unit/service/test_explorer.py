import os
import pytest
from src.model.creature import Creature
from src.errors import Missing, Duplicate
from src.data import creature

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"

@pytest.fixture
def sample() -> Creature:
    return Creature(name="yeti", country="CN", area="Himalayas", description="Harmless Himalayan", aka="Abominable Snowman")

def test_create(sample: Creature):
    resp = creature.create(sample)
    assert resp == sample

def test_create_duplicate(sample: Creature):
    with pytest.raises(Duplicate):
        _ =  creature.create(sample)

def test_get_one(sample: Creature):
    resp = creature.get_one(sample.name)
    assert resp == sample

def test_modify(sample):
    creature.area = "Sesame Street"
    resp = creature.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing(sample):
    thing: Creature = Creature(name="snurfle", country="RU", area="", description="some thing", aka="")
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)

def test_delete(sample: Creature):
    resp = creature.delete(sample.name)
    assert resp is True

def test_delete_missing(sample: Creature):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)

