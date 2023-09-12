#!/usr/bin/python3
"""
Deserializing a JSON representation to Python
"""
import json


def load_from_json_file(filename):
    """Create Object From A JSON File
    This module creates a Python object from a JSON file
    This file should contain JSON string representation of Python object

    Args:
        filename: filename of the JSON doc

    Return:
        NIL
    """

    if type(filename) is not str:
        raise TypeError("filename must be a String")

    with open(filename, "r", encoding="utf-8") as open_f:
        return json.load(open_f)
