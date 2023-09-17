#!/usr/bin/python3
"""
Testcases for Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from tests.test_models.test_base import TestBaseClass


def setUpModule():
    """sets up a module
    """

    print("setting up RectangleModule....")


def tearDownModule():
    """tears down a module
    """

    print("tearing down RectangleModule....")


class TestRectangleClass(TestBaseClass):
    @classmethod
    def setUpClass(cls):
        """sets up a class
        """

        print("setting up TestRectangleClass")
        if not issubclass(Rectangle, Base):
            raise unittest.SkipTest("Rectangle is not a subclass")

    @classmethod
    def tearDownClass(cls):
        """tears down a class
        """

        print("tearing down TestRectangleClass")

    def test_rectangle_id(self):
        """
        Testing Rectangle's ID
        """

        self.new_obj = Rectangle(2, 10)
        self.new_obj1 = Rectangle(10, 2, 0, 0, 12)
        self.new_obj2 = Rectangle(3, 5)
        self.new_obj3 = Rectangle(3, 5, 3)
        self.assertEqual(self.new_obj.id, 1)
        self.assertEqual(self.new_obj1.id, 12)
        self.assertEqual(self.new_obj2.id, 2)
        self.assertEqual(self.new_obj3.x, 3)
        self.assertEqual(self.new_obj3.id, 3)

    def test_width_and_height_not_passed(self):
        """
        Testing width and height not passed
        """

        with self.assertRaises(TypeError):
            self.new_obj = Rectangle()
        with self.assertRaises(TypeError):
            self.new_obj = Rectangle(1)

    def test_accessing_width_and_height(self):
        """
        Encapsulation tests
        """

        self.new_obj = Rectangle(2, 10)
        with self.assertRaises(AttributeError):
            self.new_obj.__width
        with self.assertRaises(AttributeError):
            self.new_obj.__height
        with self.assertRaises(AttributeError):
            self.new_obj.__x
        with self.assertRaises(AttributeError):
            self.new_obj.__y

    def test_changing_values_of_encapsulated_data(self):
        """
        Changing values of instance variables
        """

        self.new_obj1 = Rectangle(10, 2, 0, 0, 12)
        self.new_obj1.width = 5
        self.new_obj1.height = 10
        self.new_obj1.x = 20
        self.new_obj1.y = -1
        self.assertEqual(self.new_obj1.width, 5)
        self.assertEqual(self.new_obj1.height, 10)
        self.assertEqual(self.new_obj1.x, 20)
        self.assertEqual(self.new_obj1.y, -1)
