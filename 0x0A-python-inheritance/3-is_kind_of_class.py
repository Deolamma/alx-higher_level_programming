#!/usr/bin/python3
"""
This module checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an arg is an instance of a class or
    an instance of a class that inherited from the specified class

    Args:
        obj: Any Object
        a_class: Any class

    Return:
        True if obj is an instance of a_class.
    """

    if type(obj) is a_class or isinstance(type(obj), a_class):
        return True
    return False
