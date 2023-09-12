#!/usr/bin/python3
"""
This module returns the dictionary rep. of a class
"""


def class_to_json(obj):
    """Class To JSON
    This module returns the dictionary rep. of an object
    This is then used for JSON serialization

    Args:
        obj; Instance of an object

    Return:
        returns the dictionary of a class
    """

    return obj.__dict__
