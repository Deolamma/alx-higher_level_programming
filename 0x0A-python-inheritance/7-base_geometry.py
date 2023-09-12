#!/usr/bin/python3
"""
Creating a Base Geometry class
"""


class BaseGeometry:
    """
        A simple class
    """
    def area(self):
        """
        A simple method

        Args:
            NIL
        Raises:
            Exception: when area is called.
        Return:
            NIL
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer

        Args:
            name: First argument passed to the method. Always string
            value: Integer to tbe validated
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        Return:
            NIL
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
