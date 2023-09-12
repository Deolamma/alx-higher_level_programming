#!/usr/bin/python3
"""
Appending text to a file
"""


def append_write(filename="", text=""):
    """Appending To A File
    Appends to the end of a file
    Creates the file if doesn't exist

    Args:
        filename: name of file to be appended
        text: Text to be appended to a file

    Return:
        returns the number of characters read
    """

    if type(filename) is not str:
        raise TypeError("Filename must be a String")

    with open(filename, "a", encoding="utf-8") as open_f:
        nc_read = open_f.write(text)
        return nc_read
