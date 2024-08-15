#!/usr/bin/env python3
'''
A module that takes two integers and returns a list of all delays
'''
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function: async routine 'task_wait_n'
    Arguments: n: int, max_delay: int
    Return: list of all the delays (float values)
    '''
    # Step 1: Create a list of coroutines
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Step 2: Use asyncio.gather to run them concurrently
    delays = await asyncio.gather(*tasks)
    # Step 3: Sort and return the list of delays
    return (delays)
