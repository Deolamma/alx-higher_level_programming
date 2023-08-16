#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    """Multiplying values of a dictionary by 2

        Args:
            a_dictionary: Dictionary to be traversed

        Returns:
            Returns a new dictionary containing a values multiplied by 2

    """

    new_dictionary = {k: 2 * v for k, v in a_dictionary.items()}
    return new_dictionary
