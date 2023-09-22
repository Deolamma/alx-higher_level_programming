#!/usr/bin/python3
"""
This is the Base class for the Models Package
It's core functionality is to handle ID generation if it's not provided
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converting python object to JSON rep

        Args:
            list_dictionaries: this is the list of dictionaries to be converted
                               to JSON rep.

        Return:
            returns the JSON str. rep of a list of dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saving a JSON string representation to a file
        This class makes use of the to_json_string method to convert
        the list objects to a JSON string representation.

        It saves the JSON string rep. to a .json file

        Args:
            list_objs: this is a list of class objects that inherits from base
                       directly or indirectly.
                       For instance: instances of Square or Rectangle class

        Return:
            NIL
        """

        if list_objs is None or len(list_objs) == 0:
            json_str = cls.to_json_string([])
        else:
            dictionary = [
                            objs.to_dictionary()
                            for objs in list_objs
                         ]
            json_str = cls.to_json_string(dictionary)

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as open_file:
            open_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """From JSON to String
        Converts from a JSON string to a to a Python object

        Args:
            json_string: This is the JSON string rep. to be converted to
                         a Python object

        Return:
            Returns an empty list if json_string is None or empty,
            Returns a Python obj. of the json_string rep.
        """

        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of class
        This class uses the update method to assign attributes
        to a new instance of the class

        Args:
            dictionary: this is a variable length of named arguments
                        serves as the attributes for the new object

        Return:
            Returns an instance with all attributes set
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy_inst = cls(2)
            else:
                dummy_inst = cls(2, 2)
        dummy_inst.update(**dictionary)
        return dummy_inst
