import asyncio

async def gather_all(coros, limit: int = 10):
    """Bounded fan-out. Never call blocking I/O here - use asyncio.to_thread."""
    sem = asyncio.Semaphore(limit)
    async def one(c):
        async with sem:
            return await c
    return await asyncio.gather(*(one(c) for c in coros))
