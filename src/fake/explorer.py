from src.model.explorer import Explorer

_explorers = [
    Explorer(name="Cloude Hande", country="FR", description="Scarce during full moons"),
    Explorer(name="Noah Weiser", country="DE", description="Myopic machete man"),
]

def get_all() -> list[Explorer]:
    return _explorers

def get_one(name: str) -> Explorer | None:
    for  _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    return explorer

def modify(explorer: Explorer) -> Explorer:
    return explorer

def replace(explorer: Explorer) -> Explorer:
    return explorer

def delete(explorer: Explorer) -> Explorer:
    return explorer
