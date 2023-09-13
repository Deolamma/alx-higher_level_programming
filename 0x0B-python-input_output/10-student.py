#!/usr/bin/python3
"""
This is a simple class
"""


class Student:
    """
    This is a class with one method that retrieves,
    The dictionary the dictionary representation of its instance
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation Method
        This method instantiates the Student class with 3 public attributes

        Args:
            firstname: Name of Student
            last_name: Surname of Student
            age: Age of Student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary Representation
        This module retrieves the dictionary rep. of an instance

        Args:
            attrs: A list containing keys
                   Keys should be valid attributes of the class

        Return:
            returns a json rep. of the attributes of the class if attrs = None
            if attrs is not None, return only valid attributes of the class
            in dict
        """
        if attrs is not None:
            return {
                    attribute: getattr(self, attribute) for attribute in attrs
                    if hasattr(self, attribute)
                   }
        return self.__dict__
