from fastapi import FastAPI, Body, Header, APIRouter, Response

routes = APIRouter(tags=["Chapter 4. Async, Concurrency and Starlette Tour"])

@routes.get("/greet/hi", summary="4-6. Небольшой эндпонит с асинхронностью")
async def great():
    await asyncio.sleep(3)
    return f"Hello, World!"

