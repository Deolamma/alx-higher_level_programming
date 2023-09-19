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

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

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

    def update(self, *args, **kwargs):
        """Updating attributes of Square

        Note:
            if args exist kwargs should be ignored

        Args:
            *args: depicts variable length of positional argument
            **kwargs: depicts variable of length of named argument

        Return:
            NIL
        """

        args_len = len(args)

        if args and args_len != 0:
            if args_len == 1:
                self.id = args[0]
            elif args_len <= 4:
                for i in range(args_len):
                    if i == 0:
                        setattr(self, "id", args[i])
                    if i == 1:
                        setattr(self, "size", args[i])
                    if i == 2:
                        setattr(self, "x", args[i])
                    if i == 3:
                        setattr(self, "y", args[i])
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
