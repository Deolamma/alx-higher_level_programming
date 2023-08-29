#!/usr/bin/python3
"""
This is a class with a private instance attribute
"""


class Square:

    """Creates a class with a private instance attribute
        Note:
            size is private.
        Attributes:
            size: Private instance of the class
                  It receives the size of the square passed by the object
    """
    def __init__(self, size=0):

        """This is where instantiation takes place

            Args:
                size: size of square passed by object of class
                      if None, size defaults to 0
            Raises:
                ValueError: This is raised if size is less than zero
                TypeError: Raises error if size is not an integer
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square

            Args:
                NIL

            Returns:
                Returns the area of a square
        """
        area_of_square = self.__size * self.__size

        return area_of_square
