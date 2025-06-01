import asyncio

async def q():
    await print("Why can't programmers tell jokes?")
    await asyncio.sleep(3)

async def a():
    await print("Timing!")

async def main():
    await asyncio.gather(q(), a())

asyncio.run(main())
