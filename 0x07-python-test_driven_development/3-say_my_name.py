#!/usr/bin/python3
"""
This method prints the Firstname and Lastname embedded in a message
For Example:
say_my_name("John", "Smith") == "My name is John Smith"
Only Strings are valid arguments
"""


def say_my_name(first_name, last_name=""):

    """
    Printing Two String Arguments

    Args:
        first_name: first string to be passed and reps firstname of user
        last_name: second string to be passed and reps surname of user

    This module prints two string arguments emebeded in a message.
    strings have to be only of string type and last_name should default to

    Returns:
        Returns nothing. Prints message to standard out
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if last_name is None:
        last_name = " "
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # Checks that there's no space between first_name
    if first_name is not None:
        for char in first_name:
            if len(first_name) > 1:
                if char == " ":
                    raise TypeError("first_name cannot contain space")
    # checks that there's no space between last-name string
    if last_name is not None:
        for char_2 in last_name:
            if len(last_name) > 1:
                if char_2 == " ":
                    raise TypeError("last_name cannot contain space")
    print("My name is {} {}".format(first_name, last_name))
