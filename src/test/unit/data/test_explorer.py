import os
import pytest
from src.model.explorer import Explorer
from src.errors import Missing, Duplicate
from src.data import explorer

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"

@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="John Doe", country="RU", description="Human Explorer")

def test_create(sample: Explorer):
    resp = explorer.create(sample)
    assert resp == sample

def test_create_duplicate(sample: Explorer):
    with pytest.raises(Duplicate):
        _ =  explorer.create(sample)

def test_get_one(sample: Explorer):
    resp = explorer.get_one(sample.name)
    assert resp == sample

def test_modify(sample):
    explorer.description = "Sesame Street"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing(sample):
    thing: Explorer = Explorer(name="Ivan Ivanov", country="UK", description="some thing")
    with pytest.raises(Missing):
        _ = explorer.modify(thing.name, thing)

def test_delete(sample: Explorer):
    resp = explorer.delete(sample.name)
    assert resp is True

def test_delete_missing(sample: Explorer):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)

