#!/usr/bin/env python3
'''This module takes a list mxd_lst of integers and floats
and returns their sum as a float.'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    type-annotated function 'sum_mixed_list'
    Arguments: mxd_lst with ints and floats
    Return: sum as a flat
    '''
    return sum(mxd_lst)
