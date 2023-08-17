#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    """Deleting all keys containing a given value

        Args:
            a_dictionary: Dictionary to be traversed
            value: Value to be checked in dictionary

        Returns:
            Returns an updated dictionary with deleted keys
    """

    keys_to_delete = [k for k, v in a_dictionary.items() if v == value]
    for element in keys_to_delete:
        del a_dictionary[element]
    return a_dictionary
