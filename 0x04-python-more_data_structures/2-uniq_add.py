#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Summing elements once

        Args:
            my_list: List to be traversed

        Returns:
            Returns the sum of elements
    """

    new_list = set(my_list)
    result = 0

    for element in new_list:
        result += element
    return result
