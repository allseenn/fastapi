from src.model.user import User
from .init import (conn, curs, get_db, IntegrityError)
from src.errors import Missing, Duplicate

curs.execute("create table if not exists user (name text primary key, hash text)")
curs.execute("create table if not exists xuser (name text primary key, hash text)")

def row_to_model(row: tuple) -> User:
    return User(name=row[0], hash=row[1])

def model_to_dict(user: User) -> dict:
    return user.model_dump() if user else None

def get_one(name: str) -> User:
    qry = "select * from user where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"User {name} not found")

def create(user: User, table: str = "user") -> User:
    qry = f"insert into {table} values(:name, :hash)"
    params = model_to_dict(user)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"User {user.name} already exists")
    conn.commit()
    return get_one(user.name)

def modify(name: str, user: User) -> User:
    qry = "update user set name=:name, hash=:hash where name=:name0"
    params = model_to_dict(user)
    params = {
        "name": user.name,
        "hash": user.hash,
        "name0": name}
    curs.execute(qry, params)
    if curs.rowcount == 1:
        conn.commit()
        return get_one(user.name)
    else:
        raise Missing(msg=f"User {name} not found")

def delete(name: str) -> None:
    user = get_one(name)
    qry = "delete from user where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"User {name} not found")
    create(user, table="xuser")
    conn.commit()
