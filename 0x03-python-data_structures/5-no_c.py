#!/usr/bin/python3
def no_c(my_string):
    """Removing C characters from an array of strings

        Args:
            my_string: This is the string to be operated on

        Returns:
            Returns a new list without the char c or C
        """

    new_str = ""
    for index, elem in enumerate(my_string):
        if (elem == chr(67)) or (elem == chr(99)):
            continue
        new_str += elem
    return new_str
