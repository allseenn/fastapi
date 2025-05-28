from model import Creature
from fastapi import APIRouter

router = APIRouter(prefix="/web), tags=["Chapter 5. Pydantic, Type Hints, and Models Tour"]


@router.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()
