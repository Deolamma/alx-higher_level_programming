#!/usr/bin/python3
"""
This module checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Checks if two args are the same object

    Args:
        obj: Any Object
        a_class: Any class

    Return:
        True if obj is an instance of a_class.
    """

    if isinstance(obj, a_class) or type(obj) is a_class:
        return True
    return False
