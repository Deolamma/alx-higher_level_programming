"""
A class that inherits from Rectangle class
Rectangle class inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Multilevel Inheritance
    class Square inherits from Rectangle which in-turn
    inherits from BaseGeometry class
    """

    def __init__(self, size):
        """
        Instatiation method of a class
        Implements the integer_validator() of it's superclass

        Args:
            size: size of square
                  Private attribute of class
        """

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Overrides the area method of it's superclass

        Return:
            returns the area of a Square
        """

        return self.__size ** 2
