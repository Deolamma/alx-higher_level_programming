#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Determining Multiples of 2
        Args:
            my_list: List to be traversed

        Returns:
            Returns True if element is a multiple of 2
    """

    if not my_list:
        return None
    new_list = [(abs(elem % 2) == 0) for elem in my_list]
    return new_list
