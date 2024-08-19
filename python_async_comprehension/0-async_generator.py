#!/usr/bin/env python3
'''coroutine called async_generator that takes no arguments'''
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random float between 0 and 10
        yield random.uniform(0, 10)
