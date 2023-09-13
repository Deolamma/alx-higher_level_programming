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

    def to_json(self):
        """Dictionary Representation
        This module retrieves the dictionary rep. of an instance

        Args:
            NIL

        Return:
            returns the instances __dict__ rep.
        """

        return self.__dict__
