from fastapi import FastAPI
from hello import routes as hello_routes

app = FastAPI(title="FastAPI",
description="""
## Modern Python Web Development
Bill Lubanovic
""")


# Подключаем роутер из hello.py
app.include_router(hello_routes)
