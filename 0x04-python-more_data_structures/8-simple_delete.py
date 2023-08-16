#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):

    """Delete element at key

        Args:
            a_dictionary: Dictionary to be deleted from
            key: key to find

        Returns:
            Returns updated dictionary with deleted element
    """

    for k in a_dictionary:
        if k == key:
            del a_dictionary[key]
            return a_dictionary
    return a_dictionary
