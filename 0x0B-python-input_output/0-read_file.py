#!/usr/bin/python3
"""
This module reads content of a file and prints to STDOUT
"""


def read_file(filename=""):
    """Read File
    Reads a file and prints to stdout

    Args:
        filename: File to be read from

    Raises:
        TypeError: if filename is not a string

    Return:
        NIL
    """

    if type(filename) is not str:
        raise TypeError("Filename must be a String")
    with open(filename, "r", encoding="utf-8") as open_f:
        print(open_f.read().rstrip())
