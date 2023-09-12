#!/usr/bin/python3
"""
This module Serializes a Python Object and writes it to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """Save Object To File
    This module converts a Python object to it's JSON representation

    Args:
        my_obj: Python object to be serialized
        filename: file in which the JSON rep. is to be stored

    Return:
        NIL
    """

    if type(filename) is not str:
        raise TypeError("filename should be a String")

    with open(filename, "w", encoding="utf-8") as open_f:
        json.dump(my_obj, open_f)
