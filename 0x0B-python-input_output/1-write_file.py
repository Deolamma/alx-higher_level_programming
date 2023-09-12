#!/usr/bin/python3
"""
A module that writes a text to a file
"""


def write_file(filename="", text=""):
    """Write To A File
    This module writes to a given text to a file

    Args:
        filename: Name of file to be written to
        text: text to be written to file

    Raises:
        TypeError: if filename is not a string

    Return:
        returns the number of characters read
    """

    if type(filename) is not str:
        raise TypeError("Filename must be a String")

    with open(filename, 'w', encoding="utf-8") as open_f:
        nc_read = open_f.write(text)
        return nc_read
