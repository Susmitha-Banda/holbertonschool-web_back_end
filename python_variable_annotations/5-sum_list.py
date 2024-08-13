#!/usr/bin/env python3
'''this module takes a list input_list of floats as
argument and returns their sum as a float'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Type-annotated function that takes a list of floats
    Parameters:input_list (List[float]): A list containing
    floating-point numbers.
    and returns their sum as a float.'''
    return sum(input_list)
