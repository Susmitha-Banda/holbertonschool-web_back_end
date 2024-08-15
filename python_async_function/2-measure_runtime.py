#!/usr/bin/env python3
'''measures the total execution time'''
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function: 'measure_time'
    Arguments: two int's
    Return: total_time / n
    """
    # Record the start time
    start_time = time.time()
    # Run the wait_n function
    asyncio.run(wait_n(n, max_delay))
    # Record the end time
    end_time = time.time()
    # Calculate total execution time
    total_time = end_time - start_time

    # Return the average time per call
    return total_time / n
