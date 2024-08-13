#!/usr/bin/env python3
'''
module that annotates belows function parameters
and returns values with approriate types
'''
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    function element_length
    Argument: lst
    Return List
    '''
    return [(i, len(i)) for i in lst]
