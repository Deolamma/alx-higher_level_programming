#!/usr/bin/python3
"""
This class sets attribute only to attributable objects
"""


def add_attribute(obj, key, value):
    """Setting Attributes
    This class attempts to set attributes to objects

    Args:
        obj: object whose attribute is to be set
        key: key of the attribute
        value: value of the attribute

    Raises:
        TypeError: Is raised if obj is not attributable
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
