#!/usr/bin/env python3
"""a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a
function that multiplies a float by multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier as argument and returns a
    function that multiplies a float by multiplier
    """
    def fn(float):
        return multiplier * float
    return fn