#!/usr/bin/python3
"""
This module prints a square using # for a given 'size'
'size' has to be a valid integer
For Example:
    print_squar(4) ==
    ####
    ####
    ####
    ####

"""


def print_square(size):
    """
    Printing a Square
    This module prints a square using # when given a valid size

    Args:
        size: is a valid +ve int or +ve float number
        For Example:
         size CANNOT be -4.0 OR -4
         size CANNOT be "String"

    Return:
        Returns nothing
    """

    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, (int, float)):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    for i in range(int(size)):
        for j in range(int(size)):
            print("{}".format("#" if (int(size) > 0) else "\n"), end="")
        print()
