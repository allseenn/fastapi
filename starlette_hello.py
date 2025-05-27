#!/usr/bin/env python
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

async def greeting(request):
    return JSONResponse({"hello": "world"})

app = Starlette(debug=True, routes=[
    Route("/hi", greeting),])

app = Starlette(debug=True, routes=[
    Route("/hi", greeting),])

if __name__ == "__main__":
    uvicorn.run("starlette_hello:app", reload=True)
