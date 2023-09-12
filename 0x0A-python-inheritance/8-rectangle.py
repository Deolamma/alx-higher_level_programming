#!/usr/bin/python3
"""
A simple class that inherits from BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from the BaseGeometry class
    """

    def __init__(self, width, height):
        """
        Instatiation method for Rectangle class
        Args are to be validated by integr_validator method of BaseGeometry

        Args:
            width: width of Rectangle
            height: height of Rectangle

        Returns:
            NIL
        """

        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height ", self.__height)
