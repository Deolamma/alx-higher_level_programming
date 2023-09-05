#!/usr/bin/python3
"""
Rectangle is a class that has 2 properties
Encapsulation is practiced here
Raises an error if any of the property values are not valid integers
Prints a rectangle using # symbol
"""


class Rectangle:

    """
    Setting Width and Height Property of Rectangle

        Note:
            Width and Height are private instance attribute

        Attributes:
            width: Private instance of the class
                   It receives the width of rectangle and must be an integer
            Height: Private instance of the class
                    It receives the height of the class and must be an integer
    """

    def __init__(self, width=0, height=0):

        """
        Initializes Instance Of The Class

        Args:
            width: width of rectangle passed by object of the class
                   if None, width defaults to 0
            height: height of the rectangle passef by object of the class
                    if None is passed, height defaults to 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves The Width Of A Rectangle

        Setter Args:
            value: width of rectangle to be retrieved

        Raises:
            ValueError: Raised when the value is less than zero
            TypeError: Raised when the value is not an integer

        Return:
            Returns the width of a rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves The height Of A Rectangle

        Setter Args:
            value: height of rectangle to be retrieved

        Raises:
            ValueError: Raised when the value is less than zero
            TypeError: Raised when the value is not an integer

        Return:
            Returns the height of a rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates The Area of A Rectangle

        A public instance method that prints an area of a rectangle

            Args:
                NIL

            Return:
                Area of a rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates The Perimeter Of A Rectangle

        A public instance method that calculates the perimeter of a rectangle

        Args:
            NIL

        Return:
            Returns the perimeter of a rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
