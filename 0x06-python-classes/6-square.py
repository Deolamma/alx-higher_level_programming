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
            Position: Defines the number of spaces to move
                      before creating square.
        Note:
            Spaces should not be created if postion[1] > 0
    """

    def __init__(self, size=0, position=(0, 0)):

        """This is where instantiation takes place

            Args:
                size: size of square passed by object of class
                      if None, size defaults to 0
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Retrieves the Position tuple

            Setter Args:
                Value: Tuple containig values for number of spaces to be moved

            Raises:
                TypeError: Raised if position is NOT a tuple
                            of 2 positive integers


            Returns:
                Returns the position tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (
            (type(value) is not tuple) or (len(value) != 2) or
            (value[0] < 0) or (value[1] < 0) or (type(value[0]) is not int)
            or (type(value[1]) is not int)
           ):
            print("I got here _______________________")
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for i in range(self.position[0]):
                print(" ", end="")
            for i in range(self.size):
                print("#", end="")
            print()
