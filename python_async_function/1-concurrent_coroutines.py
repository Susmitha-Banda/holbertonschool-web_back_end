#!/usr/bin/env python3
'''
multiple coroutines at the same time with async
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function: async routine 'wait_n'
    Arguments: n: int, max_delay: int
    Return: list of all the delays (float values)
    '''
    # Step 1: Create a list of coroutines
    coroutines = [wait_random(max_delay) for _ in range(n)]
    # Step 2: Use asyncio.gather to run them concurrently
    delays = await asyncio.gather(*coroutines)
    # Step 3: Sort and return the list of delays
    return sorted(delays)
