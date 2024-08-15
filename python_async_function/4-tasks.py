#!/usr/bin/env python3
"""Nameless module for Python Async Task 1"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """calls wait_random n number of times"""

    delays = []
    tasks = []
    for x in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
