from fastapi import FastAPI
from hello import routes as hello_routes
from greet_async import routes as greet_routes
from web import routes as web_routes
from dependency import routes as dep_routes

app = FastAPI(title="FastAPI",
description="""
## Modern Python Web Development
Bill Lubanovic
""")

# Подключаем роутер из hello.py
app.include_router(hello_routes)
app.include_router(greet_routes)
app.include_router(web_routes)
app.include_router(dep_routes)
