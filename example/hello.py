# 3 3-1 3-11
from fastapi import FastAPI, Body, Header, APIRouter, Response

routes = APIRouter(prefix="/api/hello", tags=["Chapter 3. FastAPI Tour"])

@routes.get("/hi", summary="3-1. запрос без передачи информации")
def no_param_greet():
    """
```uv run http localhost:8000/hi```
    """
    return f"1. NO params"


@routes.get("/hi/{who}", summary="3-11. передача информации с помощью директории в адресе")
def url_greet(who):
    """
С помощощью библиотеки http можно послать GET-запрос и получить ответ от fastapi приложения

```uv run http localhost:8000/hi/name```
    """
    return f"2. URL PATH, {who}?"


@routes.patch("/hi", summary="3-15. передача информации с помощью ключ-значение в адресе")
def query_greet(who):
    """
```uv run http PATCH localhost:8000/hi?who=name```
    """
    return f"3. QUERY PARAMS, {who}?"


@routes.post("/hi", summary="3-21. передача информации в теле запроса")
def body_greet(who:str=Body(embed=True)):
    """
```uv run http -v POST localhost:8000/hi who=name```
    """
    return f"4. BODY, {who}?"


@routes.put("/hi", summary="3-24. передача информации в заголовке запроса")
def header_greet(who:str = Header()):
    """
```uv run http -v PUT localhost:8000/hi who:name```
    """
    return f"5. HEADER, {who}?"


@routes.get("/agent", summary="3-26. вывод информации из заголовка запроса")
def get_agent(user_agent:str = Header()):
    return user_agent


code=402
@routes.get("/happy", status_code=code, summary="3-28. инъекция кода состояния")
def greet():
    return code


@routes.get("/header/{name}/{value}", summary="3-31. инъекция HTTP-заголовков в ответе")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

