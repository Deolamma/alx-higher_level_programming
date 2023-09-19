#!/usr/bin/python3
"""
A square class that inherits from a rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a special square class that inherits from the rectangle class
    Validation of it's instance attributes are done by the rectangle class

    Note:
        Square is a special rectangle so size data replaces,
        both width and height of rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Overriding the rectangle class init method

        Args:
            size: This is the size of the square
            x: x-axis data, used to determine how much space should be kept
               before drawing of shape on the x-axis
            y: y-axis data, used to determine how much space should be kept
               before drawing of shape on the y-axis
            id: Id of shape

        Note: size would replace the width and height attr. of rectangle
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of an instance of square

        Return:
            returns the string rep. of an instance
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Encapsulation of size attribute
        Inherits the data validation of width in the rectangle class

        Return:
            returns the size(width) of square
        """

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
