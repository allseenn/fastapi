# 4-6
from fastapi import Body, Header, APIRouter, Response

routes = APIRouter(prefix="/api/greet", tags=["Chapter 4. Async, Concurrency and Starlette Tour"])

@routes.get("/hi", summary="4-6. Небольшой эндпонит с асинхронностью")
async def great():
    await asyncio.sleep(3)
    return f"Hello, World!"

