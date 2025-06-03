#!/usr/bin/env python3
"""
4-4 Example of async joke
"""
import asyncio

async def q():
    print("Why can't programmers tell jokes?")
    await asyncio.sleep(3)

async def a():
    print("Timing!")

async def main():
    await asyncio.gather(q(), a())

if __name__ == "__main__":
    print(__doc__)
    asyncio.run(main())
