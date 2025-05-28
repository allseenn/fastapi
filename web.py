from model import Creature
from fastapi import APIRouter

routes = APIRouter(prefix="/api/web", tags=["Chapter 5. Pydantic, Type Hints, and Models Tour"])


@routes.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()
