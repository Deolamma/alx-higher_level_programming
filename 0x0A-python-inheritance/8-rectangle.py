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

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height ", height)
        self.__height = height
