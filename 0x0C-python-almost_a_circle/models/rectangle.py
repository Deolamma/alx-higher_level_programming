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

    @property
    def width(self):
        """Encapsulating the Width Property
        This method encapsulates the width property of the instance

        Args:
            value: this is the value to be set for the width

        Return:
            Returns the width passed to the instance
        """

        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Encapsulating the height Property
        This method encapsulates the height property of the instance

        Args:
            value: this is the value to be set for the width

        Return:
            Returns the height passed to the instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Encapsulating the x property
        This method encapsulates the x property of the instance

        Args:
            value: this is the value to be set fir the x property

        Returns:
            Returns the x value set or 0
        """

        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Encapsulating the x property
        This method encapsulates the x property of the instance

        Args:
            value: this is the value to be set fir the x property

        Returns:
            Returns the x value set or 0
        """

        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
