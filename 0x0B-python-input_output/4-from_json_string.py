#!/usr/bin/python3
"""
This module deserializes a string
"""
import json


def from_json_string(my_str):
    """From JSON To Object
    conerts a JSON string to a Python Object

    Args:
        my_str: JSON string to be deserialized

    Returns:
        returns a Python object
    """

    if type(my_str) is not str:
        raise TypeError("JSON must be string")

    return json.loads(my_str)
