#!/usr/bin/python3
"""
Serializing an Object
"""
import json


def to_json_string(my_obj):
    """To JSON String
    converts a python object to its JSON representation

    Args:
        obj: Python object to be serialized

    Return:
        returns the JSON serialized representation
    """

    return json.dumps(my_obj)
