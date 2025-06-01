#!/usr/bin/env .venv/bin/python
# общие импорты
from fastapi import FastAPI
# импорты из примеров
from examples.hello import routes as hello_routes
from examples.greet_async import routes as greet_routes
from examples.web import routes as web_routes
from examples.dependency import routes as dep_routes
# импорты основной программы
from src.web import explorer, creature

app = FastAPI(title="FastAPI",
description="""
## Modern Python Web Development
Bill Lubanovic
""")

# Подключаем роутеры из пакета examples
app.include_router(hello_routes)
app.include_router(greet_routes)
app.include_router(web_routes)
app.include_router(dep_routes)

# Подключаем роутеры из основного пакета приложения src
app.include_router(explorer.router)
app.include_router(creature.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)