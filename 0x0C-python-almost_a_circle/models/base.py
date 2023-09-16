#!/usr/bin/python3
"""
This is the Base class for the Models Package
It's core functionality is to handle ID generation if it's not provided
"""


class Base:
    """Base Class
    This class generates an ID for it's subclasses if one is not provided
    It does this using the private class attribute __nb_objects

    Attributes:
        nb_objects: This is a private class attribute which is incremented
                    and assigned to ID if an object is instantiatied,
                    without an ID
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiator
        This method instantiates an object with the ID provided
        If no ID is provided it assigns one to the object after incrementing
        the private class attribute nb_objects

        Args:
            id: This is a public instance attribute
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
