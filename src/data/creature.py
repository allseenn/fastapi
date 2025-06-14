from .init import (conn, curs, IntegrityError)
from src.model.creature import Creature
from src.errors import Missing, Duplicate

curs.execute("create table if not exists creature (name text primary key, description text, country text, area text, aka text)")

def row_to_model(row: tuple) -> Creature:
    return Creature(name=row[0], description=row[1], country=row[2], area=row[3], aka=row[4])

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump() if creature else None

def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Creature {name} not found")

def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(creature: Creature) -> Creature:
    qry = "insert into creature values(:name, :description, :country, :area, :aka)"
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"Creature {creature.name} already exists")
    conn.commit()
    return get_one(creature.name)

def modify(name: str, creature: Creature) -> Creature:
    qry = "update creature set description=:description, country=:country, area=:area, aka=:aka where name=:name"
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        conn.commit()
        return get_one(creature.name)
    else:
        raise Missing(msg=f"Creature {name} not found")

def delete(name: str) -> bool:
    qry = "delete from creature where name=:name"
    params = {"name": name}
    res = curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Creature {name} not found")
    conn.commit()
    return bool(res)

