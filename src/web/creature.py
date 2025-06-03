from fastapi import APIRouter
from src.model.creature import Creature
import src.data.creature as service

router = APIRouter(prefix="/creature", tags=["Chapter 8. Web app"])

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name: str) -> Creature | None:
    return service.get_one(name)

@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/{name}")
def modify(creature: Creature) -> Creature:
    return service.modify(creature)

@router.put("/")
def replace(creature: Creature) -> Creature:
    return service.replace(creature)

@router.delete("/{name}")
def delete(dname: str):
    return None
