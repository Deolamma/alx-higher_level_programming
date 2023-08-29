#!/usr/bin/python3
"""
This is a class with a private instance attribute
"""


class Square:

    """Creates a class with a private instance attribute
        Note:
            size is private.
        Args:
            size: Private instance of the class
                  It receives the size of the square passed by the object
    """
    def __init__(self, size):

        """This is where instantiation takes place

            Args:
                size: size of square passed by object of class
        """
        self.__size = size
