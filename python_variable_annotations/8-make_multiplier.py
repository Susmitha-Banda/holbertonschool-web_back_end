#!/usr/bin/env python3
''' takes a float multiplier as argument and returns a
function that multiplies a float by multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    function 'make_multiplier'
    Args: float
    Return: function that multiplies
    '''
    def multiplier_func(x: float) -> float:
        return (x * multiplier)
    return multiplier_func
