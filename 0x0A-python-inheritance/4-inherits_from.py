#!/usr/bin/python3
"""
This module checks if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    Checks if an arg is an instance of a class that
    inherited  directly or indirectly from a specified class

    Args:
        obj: Any Object
        a_class: Any class

    Return:
        True if obj is an instance of a_class that inherited
        directly or indirectly.
    """

    if issubclass(type(obj), a_class) and (type(obj) is not a_class):
        return True
    return False
