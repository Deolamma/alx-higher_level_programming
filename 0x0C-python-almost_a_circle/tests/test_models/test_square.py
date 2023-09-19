#!/usr/bin/python3
"""
Testcases for Square class
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.square import Square
from tests.test_models.test_rectangle import TestRectangleClass


def setUpModule():
    """sets up a module
    """

    print("setting up SquareModule....")


def tearDownModule():
    """tears down a module
    """

    print("tearing down SquareModule....")


class TestSquareClass(TestRectangleClass):
    @classmethod
    def setUpClass(cls):
        """sets up a class
        """

        print("setting up TestSquareClass")
        if not issubclass(Square, Rectangle):
            raise unittest.SkipTest("Square is not a subclass of Rectangle")

    @classmethod
    def tearDownClass(cls):
        """tears down a class
        """

        print("tearing down TestSquareClass")

    def test_square(self):
        """Testing Square class"""

        self.obj = Square(5)
        self.assertEqual(self.obj.size, 5)
        self.assertEqual(self.obj.width, 5)
        self.assertEqual(self.obj.height, 5)
        self.assertEqual(self.obj.x, 0)
        self.assertEqual(self.obj.y, 0)
        self.assertEqual(self.obj.id, 1)

        self.obj1 = Square(5, 3)
        self.assertEqual(self.obj1.size, 5)
        self.assertEqual(self.obj1.width, 5)
        self.assertEqual(self.obj1.height, 5)
        self.assertEqual(self.obj1.x, 3)
        self.assertEqual(self.obj1.y, 0)
        self.assertEqual(self.obj1.id, 2)

    def test_square2(self):
        """Testing Square class with full arguments"""
        self.obj = Square(5, 4, 4, 3)
        self.assertEqual(self.obj.size, 5)
        self.assertEqual(self.obj.width, 5)
        self.assertEqual(self.obj.height, 5)
        self.assertEqual(self.obj.x, 4)
        self.assertEqual(self.obj.y, 4)
        self.assertEqual(self.obj.id, 3)

    def test_valid_attr(self):
        """Testing valid attribute passed"""
        with self.assertRaises(TypeError):
            self.obj = Square("5")
        with self.assertRaises(TypeError):
            self.obj = Square(2, "2", 3, 4)
        with self.assertRaises(TypeError):
            self.obj = Square(False)

    def test_valid_attr_1(self):
        """Testing valid attribute passed"""
        with self.assertRaises(ValueError):
            self.obj = Square(0)
        with self.assertRaises(ValueError):
            self.obj = Square(5, -2)

    def test_square_instances(self):
        """Testing if instances are same"""

        self.obj = Square(2, 3)
        self.obj1 = Square(2, 3)
        self.assertEqual(False, self.obj is self.obj1)
        self.assertEqual(False, self.obj.id == self.obj1.id)

    def test_no_attr_passed(self):
        """
        Testing width and height not passed
        """

        with self.assertRaises(TypeError):
            self.new_obj = Square()

    def test_too_many_attr_passed(self):
        """
        Testing too many arguments passed
        """

        with self.assertRaises(TypeError):
            self.new_obj = Square(1, 2, 3, 4, 5)

    def test_accessing_private_attributes(self):
        """
        Encapsulation tests
        """

        self.new_obj = Square(2, 10)
        with self.assertRaises(AttributeError):
            self.new_obj.__width

    def test_accessing_private_attributes_1(self):
        """
        Encapsulation tests
        """

        self.new_obj = Square(2, 10)
        with self.assertRaises(AttributeError):
            self.new_obj.__height

    def test_accessing_private_attributes_2(self):
        """
        Encapsulation tests
        """

        self.new_obj = Square(2, 10)
        with self.assertRaises(AttributeError):
            self.new_obj.__x

    def test_accessing_private_attributes_3(self):
        """
        Encapsulation tests
        """

        self.new_obj = Square(2, 10)
        with self.assertRaises(AttributeError):
            self.new_obj.__y

    def test_str(self):
        """Testing __str__method of Square"""

        self.obj = Square(5)
        result = "[Square] (1) 0/0 - 5\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_str1(self):
        """
        Testing that proper id is printed out if nothing is passed for id, x, y
        """

        self.obj = Square(2, 5)
        result = "[Square] (1) 5/0 - 2\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_str2(self):
        """
        Testing that proper str rep. is printed out when width is changed
        """

        self.obj = Square(2, 5, 6, 12)
        result = "[Square] (12) 5/6 - 2\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

        # Changing the value for width
        self.obj.size = 4
        result = "[Square] (12) 5/6 - 4\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_area_of_square(self):
        """Test area of square"""

        self.obj = Square(2, 3)
        self.assertEqual(self.obj.area(), 4)

    def test_area_of_square2(self):
        """Test area of square after changing width"""

        self.obj = Square(10, 5)
        self.obj.size = 2
        self.assertEqual(self.obj.area(), 4)

    def test_diplay(self):
        """Testing that display prints a proper square"""

        self.obj = Square(2)
        result = "##\n##\n"
        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

        # Change x and y axis data
        self.obj.x = 2
        self.obj.y = 1
        result = "\n  ##\n  ##\n"
        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

    def test_display2(self):
        """Recreate square after changing height"""

        self.obj = Square(2, 3, 1, 0)
        result = "\n   ##\n   ##\n"
        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

        self.obj.size = 5
        result = "\n   #####\n   #####\n   #####\n   #####\n   #####\n"
        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)
