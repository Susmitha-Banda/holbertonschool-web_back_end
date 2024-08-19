#!/usr/bin/env python3
'''coroutine called async_generator that takes no arguments'''
import random
import asyncio


async def async_generator():
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random float between 0 and 10
        yield random.uniform(0, 10)
