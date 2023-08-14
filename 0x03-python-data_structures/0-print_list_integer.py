#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Printing a list of integers
    Args:
        my_list: List to be looped through

    Returns:
        Returns nothing.
    """

    for elem in my_list:
        print("{:d}".format(elem))
