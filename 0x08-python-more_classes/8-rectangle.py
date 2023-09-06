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
            number_of_instances: Public class attribute
                                 It is incremented during instance intiializati
                                 It is decremented during instance destruction
            print_symbol: Public class attribute.
                          It should replace the char being printed by __str__

        Static Methods:
            def bigger_or_equal(rect_1, rect_2):Returns the bigger rectangle
                                                based on area of each rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        """
        Initializes Instance Of The Class

        Args:
            width: width of rectangle passed by object of the class
                   if None, width defaults to 0
            height: height of the rectangle passef by object of the class
                    if None is passed, height defaults to 0
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __repr__(self):
        """
        Prints A String Representation Of A Rectangle Object

        For Example:
            my_rectangle = Rectangle(2, 4)
            eval(repr(my_rectangle)) Should return:
            An object of the Rectangle class

        Return:
            Returns a string rep. of a rectangle class object
        """

        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __str__(self):
        """
        Prints A String Representation
        Prints a string rep. of a rectangle using # symbol

        Args:
            NIL

        Return:
            Created rectangle with # symbol
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        created_rec = ""
        for _ in range(self.__height):
            # str Rectabgle.print_symbol returns string representatiion
            # of any type
            created_rec += (str(self.print_symbol) * self.__width) + "\n"
        return created_rec[:-1]

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Biggest Rectangle Instance
        This method returns the bigger rectangle between rect_1 and rect_2
        It does this based on the areas of these instances

        Args:
            rect_1: Instance of class Rectangle
            rect_2: Instance of class Rectangle

        Raises:
            TypeError: If either of the arguments is not instance of Rectangle

        Return:
            Returns the bigger of the two instances area OR
            rect_1 if the areas are equal
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()
        if rect_1_area >= rect_2_area:
            return rect_1
        return rect_2

    def __del__(self):
        """
        Destructor

        prints a message when an instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
