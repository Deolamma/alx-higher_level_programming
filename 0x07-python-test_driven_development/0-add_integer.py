#!/usr/bin/python3
"""
This is a module that sums integers and floats.
It returns int irrespective of the type (int or float)
"""


def add_integer(a, b=98):

    """Adds Two Integer or Float Values
    This module sums two integers and floats, for example:
        add_integer(2, 2) == 4
        add_integer(2) == 100

    Args:
        a: first operand
        b: second operand

    Return:
        Returns an int value irrespective of the type(int or float) passed
    """

    if a is None and b is None:
        raise TypeError("a and b must be integers")
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(a, bool):
        raise TypeError("a must be an integer")
    elif isinstance(b, bool):
        raise TypeError("b must be an integer")
    elif ((a + 1) == a) or ((b + 1) == b):
        raise OverflowError("a or b too large")
    result = int(a) + int(b)
    return result
