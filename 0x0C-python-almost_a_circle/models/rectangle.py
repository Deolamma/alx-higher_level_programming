#!/usr/bin/python3
"""
This is a simple class that defines properties of the instance object
This class inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class
    This class inherits from Base class
    It defines properties of the base class and properly encapsulates data
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiator
        This method instantiates objects of the class

        Note:
            This method inherits from the Base class' init method
            It depends on it to handle ID generation

        Args:
            width: width of rectangle, private property
            height: height of rectangle, private property
            x: a private property of the instance
            y: a private property of the instance

        Return:
            NIL
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """returns a string rep. of the instance of the class

        Returns:
            returns a string rep. of the instance of the class
        """

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    @property
    def width(self):
        """Encapsulating the Width Property
        This method encapsulates the width property of the instance

        Args:
            value: this is the value to be set for the width

        Raises:
            TypeError: if value is not an int data
            ValueError: if value is <= 0

        Return:
            Returns the width passed to the instance
        """

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is bool or type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Encapsulating the height Property
        This method encapsulates the height property of the instance

        Args:
            value: this is the value to be set for the width

        Raises:
            TypeError: if value is not an int data
            ValueError: if value is <= 0

        Return:
            Returns the height passed to the instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is bool or type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Encapsulating the x property
        This method encapsulates the x property of the instance

        Args:
            value: this is the value to be set fir the x property

        Raises:
            TypeError: if value is not an int data
            ValueError: if value is < 0

        Returns:
            Returns the x value set or 0
        """

        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is bool or type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Encapsulating the x property
        This method encapsulates the x property of the instance

        Args:
            value: this is the value to be set fir the x property

        Raises:
            TypeError: if value is not an int data
            ValueError: if value is < 0

        Returns:
            Returns the x value set or 0
        """

        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is bool or type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of Rectangle

        Returns:
            The Area of a Rectangle object
        """
        return (self.__width * self.__height)

    def display(self):
        """Creating a Rectangle shape
        This is a public instance method that creates a rectangle shape
        This method creates the shape using the height and width specified

        Note:
            it prints spaces equivalent to the number specified for
            x(x-axis) and y(y-axis) data
            For instance: Rectangle(2, 3, 2, 2): will print:
                          "\n\n ##\n ##\n ##\n"
        """

        create_rec = ""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            create_rec += (
                    ("{}".format(" " * self.__x if self.__x != 0 else "")) +
                    ("#" * self.__width) + "\n")
        print(create_rec[:-1])

    def update(self, *args):
        """Updating attributes of an instance
        This class updates each attribute of an instance appropriately

        Args:
            args: this is a an argument that depicts that an unknown amount
                  of data will be passed as argument

        Returns:
            NIL
        """

        args_len = len(args)
        if args_len == 1:
            self.id = args[0]
        elif args_len > 1 and args_len <= 5:
            for i in range(args_len):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
