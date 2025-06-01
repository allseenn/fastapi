from fastapi import FastAPI, Depends, APIRouter, params

def check_param(name: str = params.Param, password: str = params.Param):
    if not name:
        raise
    return {"name": name, "valid": True}

def check_query(name: str = params.Query, password: str = params.Query):
    if not name:
        raise
    return {"name": name, "valid": True}

routes = APIRouter(prefix="/api/dependency", dependencies=[Depends(check_param), Depends(check_query)],  tags=["Chapter 6. Dependencies Tour"])


@routes.get("/check_user", summary="6-1. Функция зависимостей с помощью суперкласса Param")
def check_user(user: dict = Depends(check_param)) -> dict:
    return user

@routes.post("/check_user", summary="6-5. Функция зависимостей с помощью подкласса Query в составе маршрута зависимостей")
def check_user(user: dict = Depends(check_query)) -> dict:
    return user

