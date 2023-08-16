#!/usr/bin/python3
def max_integer(my_list=[]):
    """Printing max integer in a list
        Args:
            my_list: List to be worked with

        Returns:
            Returns max integer in the given list or None
    """

    if not my_list:
        return None
    n = my_list[0]
    for element in my_list:
        n = element if element > n else n
    return n
