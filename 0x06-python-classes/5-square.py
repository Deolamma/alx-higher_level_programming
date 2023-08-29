#!/usr/bin/python3
"""
This is a class with a private instance attribute
calculates the area of a square
prints a square using the # symbol based on size passed by user
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
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of a square

            Setter Args:
                value: Size of square to be set

            Raises:
                ValueError: Raised when the value is less than zero
                TyperError: Raised when the value is not an integer

            Returns:
                Returns the size of a square
        """

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of a square

            Args:
                NIL

            Returns:
                Returns the area of a square
        """

        area_of_square = self.__size * self.__size

        return area_of_square

    def my_print(self):
        """Prints a Square Based on the size defined by user

            Args:
                NIL

            Returns:
                Returns Nothing
        """

        if self.size == 0:
            print()
        for i in range(self.size):
            for i in range(self.size):
                print("#", end="")
            print()
