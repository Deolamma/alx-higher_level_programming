#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):

    """Updating a dictionary

        Args:
            a_dictionary: Dictionary to be updated
            key: key of new elemnent in dictionary
            value: value of new element in dictionary

        Returns:
            Returns updated dictionary
    """

    for k, v in a_dictionary.items():
        if k == key:
            a_dictionary[key] = value
    a_dictionary[key] = value
    return a_dictionary
