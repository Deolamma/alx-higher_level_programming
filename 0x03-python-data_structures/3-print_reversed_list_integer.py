#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Printing a list in reverse order

        Args:
            my_list: List to be printed in reverse order

        Returns:
            Returns Nothing
        """

    for elem in my_list[::-1]:
        print("{:d}".format(elem))
