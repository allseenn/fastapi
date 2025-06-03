from fastapi import APIRouter, HTTPException
from src.model.explorer import Explorer
import src.service.explorer as service
from src.errors import Missing, Duplicate

router = APIRouter(prefix="/explorer", tags=["Chapter 8. Web app"])

@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name: str) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)

@router.patch("/{name}")
def modify(explorer: Explorer) -> Explorer:
    try:
        return service.modify(explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{name}", status_code=204)
def delete(dname: str):
    try:
        return service.delete(dname)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
