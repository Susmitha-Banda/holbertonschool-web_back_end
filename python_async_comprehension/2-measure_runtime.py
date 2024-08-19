#!/usr/bin/env python3
'''module that will execute async_comprehension 4 times '''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
      function: will execute async_c 4 times and will measure runtime
      args: none
      return: runtime
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
