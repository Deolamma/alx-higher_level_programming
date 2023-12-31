#!/usr/bin/python3
"""
unittest file for Base(id)
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def setUpModule():
    """sets up a module
    """

    print("setting up Basemodule....")


def tearDownModule():
    """tears down a module
    """

    print("tearing down Basemodule....")


class TestBaseClass(unittest.TestCase):
    """unittest for Base class
    this class will be the Base class of all other classes in this package
    """

    @classmethod
    def setUpClass(cls):
        """sets up a class
        """

        print("setting up class")

    @classmethod
    def tearDownClass(cls):
        """tears down a class
        """

        print("tearing down class")

    def setUp(self):
        """sets up before tests
        """

        print("setup")
        Base._Base__nb_objects = 0

    def tearDown(self):
        """tears down after tests
        """

        print("teardown")

    def test_init_id_values(self):
        """Tests for correct value of ID
        """
        self.obj1 = Base()
        self.obj2 = Base()
        self.obj3 = Base(8)
        self.obj4 = Base()
        self.obj5 = Base([1, 2, "emmanuel", {"name": "e", "id": 10}])
        self.obj6 = Base(-7)
        self.obj7 = Base()
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj4.id, 3)
        self.assertEqual(self.obj7.id, 4)
        self.assertEqual(self.obj3.id, 8)
        self.assertEqual(self.obj6.id, -7)
        self.assertEqual(
                          self.obj5.id, [1, 2, "emmanuel",
                                         {"name": "e", "id": 10}]
                        )

    def test_base_constructor_argument(self):
        """
        Tests that the correct number of arguments is being passed
        into base constructor
        """

        with self.assertRaises(TypeError):
            self.obj = Base(10, 30)

    def test_to_json_string(self):
        """Testing conversion to JSON str. rep."""
        json_dict = Base.to_json_string(None)
        json_dict_result = "[]\n"

        with patch("sys.stdout", StringIO()) as json_out:
            print(json_dict)
            self.assertEqual(json_out.getvalue(), json_dict_result)

    def test_to_json_string_2(self):
        """Testing conversion to JSON str. rep."""
        json_dict = Base.to_json_string([])
        json_dict_result = "[]\n"

        with patch("sys.stdout", StringIO()) as json_out:
            print(json_dict)
            self.assertEqual(json_out.getvalue(), json_dict_result)

    def test_save_to_file_square(self):
        """Testing json str rep. saved to file"""
        Square.save_to_file(None)

        with open("Square.json", "r", encoding="utf-8") as open_file:
            self.assertEqual(open_file.read(), "[]")

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_square_2(self):
        """Testing json str rep. saved to file"""
        Square.save_to_file([])

        with open("Square.json", "r", encoding="utf-8") as open_file:
            self.assertEqual(open_file.read(), "[]")

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_rectangle(self):
        """Testing json str rep. saved to file"""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r", encoding="utf-8") as open_file:
            self.assertEqual(open_file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_rectangle_2(self):
        """Testing json str rep. saved to file"""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r", encoding="utf-8") as open_file:
            self.assertEqual(open_file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_from_json_string_square(self):
        """Testing conversion of json string to Python object"""
        obj_out = Square.from_json_string(None)
        self.assertListEqual(obj_out, [])

        obj_out = Square.from_json_string([])
        self.assertListEqual(obj_out, [])

    def test_from_json_string_rectangle(self):
        """Testing conversion of json string to Pyton object"""
        obj_out = Rectangle.from_json_string(None)
        self.assertListEqual(obj_out, [])

        obj_out = Rectangle.from_json_string([])
        self.assertListEqual(obj_out, [])
