#!/usr/bin/python3
"""
Testcases for Rectangle class
"""
import unittest
from unittest.mock import patch
from io import StringIO
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
        self.new_obj4 = Rectangle(10, 2, 0, 0, -12)
        self.new_obj5 = Rectangle(10, 2, 0, 0, [2, 1, "Coder"])
        self.assertEqual(self.new_obj.id, 1)
        self.assertEqual(self.new_obj1.id, 12)
        self.assertEqual(self.new_obj2.id, 2)
        self.assertEqual(self.new_obj3.id, 3)
        self.assertEqual(self.new_obj4.id, -12)
        self.assertEqual(self.new_obj5.id, [2, 1, "Coder"])

    def test_width_and_height_not_passed(self):
        """
        Testing width and height not passed
        """

        with self.assertRaises(TypeError):
            self.new_obj = Rectangle()
        with self.assertRaises(TypeError):
            self.new_obj = Rectangle(1)

    def test_accessing_private_attributes(self):
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
        self.new_obj1.y = 1
        self.assertEqual(self.new_obj1.width, 5)
        self.assertEqual(self.new_obj1.height, 10)
        self.assertEqual(self.new_obj1.x, 20)
        self.assertEqual(self.new_obj1.y, 1)

    def test_excessive_arguments(self):
        with self.assertRaises(TypeError):
            self.new_obj = Rectangle(10, 20, -5, 10, [1, 2, "Emmanuel"], 4)

    def test_arguments_with_zero(self):
        """
        Test that valid arguments are passed to constructor of Rectangle class
        """
        # TESTS IF WIDTH OR HEIGHT IS <= ZERO
        with self.assertRaises(ValueError):
            self.obj = Rectangle(10, 10, 2, 2)
            self.obj.width = -10
        with self.assertRaises(ValueError):
            self.obj1 = Rectangle(10, -10, 2, 2)
        with self.assertRaises(ValueError):
            self.obj2 = Rectangle(0, 10, 2, 2)
        with self.assertRaises(ValueError):
            self.obj3 = Rectangle(10, 0, 2, 2)

        # TESTS FOR IF X AND Y IS >= ZERO
        with self.assertRaises(ValueError):
            self.obj4 = Rectangle(10, 10, -2, 2)
        with self.assertRaises(ValueError):
            self.obj5 = Rectangle(10, 10, 2, -2)

    def test_valid_integer_width(self):
        """
        Tests that an int data was passed for width
        """

        with self.assertRaises(TypeError):
            self.obj = Rectangle(["Emmanuel", 2], 4)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(True, 4)
        with self.assertRaises(TypeError):
            self.obj = Rectangle({"id": 4, "name": "Codec"}, 3)
        with self.assertRaises(TypeError):
            self.obj = Rectangle([], 4)
        with self.assertRaises(TypeError):
            self.obje = Rectangle(1e308, 4)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(4.0, 4)

    def test_valid_integer_height(self):
        """Tests that an int data was passed for height"""

        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, ["Emmanuel", 2])
        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, False)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(10, {"id": 4, "name": "Codec"})
        with self.assertRaises(TypeError):
            self.obj = Rectangle(3, [])
        with self.assertRaises(TypeError):
            self.obj = Rectangle(30, 1e308)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, 4.0)

    def test_valid_integer_x(self):
        """Tests that a valid int data was passed for x"""

        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, 10,  ["Emmanuel", 2])
        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, 11, False)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(10, 12, {"id": 4, "name": "Codec"})
        with self.assertRaises(TypeError):
            self.obj = Rectangle(3, 13, [])
        with self.assertRaises(TypeError):
            self.obj = Rectangle(30, 14, 1e308)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, 15, 4.0)

    def test_valid_integer_y(self):
        """Tests that a valid int data was passed for y"""

        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, 10, 1, ["Emmanuel", 2])
        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, 11,  2, False)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(10, 12, 20, {"id": 4, "name": "Codec"})
        with self.assertRaises(TypeError):
            self.obj = Rectangle(3, 13, 20, [])
        with self.assertRaises(TypeError):
            self.obj = Rectangle(30, 14, 30, 1e308)
        with self.assertRaises(TypeError):
            self.obj = Rectangle(4, 15, 40, 4.0)

    def test_area_of_rec(self):
        """Test area of rectangle"""
        self.obj = Rectangle(2, 3)
        self.assertEqual(self.obj.area(), 6)

    def test_area_of_rec2(self):
        """Test area of rectangle after changing width"""

        self.obj = Rectangle(10, 5)
        self.obj.width = 2
        self.assertEqual(self.obj.area(), 10)

    def test_area_of_rec3(self):
        """Test area of rectangle after changing height"""

        self.obj = Rectangle(10, 10)
        self.obj.height = 5
        self.assertEqual(self.obj.area(), 50)

    def test_diplay(self):
        """Testing that display prints a proper rectangle"""

        self.obj = Rectangle(2, 3)
        result = "##\n##\n##\n"
        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

        # Change x and y axis data
        self.obj.x = 2
        self.obj.y = 1
        result = result = "\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

    def test_display2(self):
        """Recreate Rec after changing height"""

        self.obj = Rectangle(2, 3, 1, 0)
        result = " ##\n ##\n ##\n"
        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

        self.obj.height = 5
        result = " ##\n ##\n ##\n ##\n ##\n"
        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

    def test_display3(self):
        """Recreate Rec after changing width"""

        self.obj = Rectangle(2, 3, 2, 2)
        result = "\n\n  ##\n  ##\n  ##\n"

        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

        self.obj.width = 4
        result = "\n\n  ####\n  ####\n  ####\n"

        with patch("sys.stdout", StringIO()) as disp_out:
            self.obj.display()
            self.assertEqual(disp_out.getvalue(), result)

    def test_str(self):
        """Testing __str__method of Rectangle"""

        self.obj = Rectangle(2, 5, 6, 7, 12)
        result = "[Rectangle] (12) 6/7 - 2/5\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_str1(self):
        """
        Testing that proper id is printed out if nothing is passed for id, x, y
        """

        self.obj = Rectangle(2, 5)
        result = "[Rectangle] (1) 0/0 - 2/5\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_str2(self):
        """
        Testing that proper str rep. is printed out when width is changed
        """

        self.obj = Rectangle(2, 5, 6, 7, 12)
        result = "[Rectangle] (12) 6/7 - 2/5\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

        # Changing the value for width
        self.obj.width = 4
        result = "[Rectangle] (12) 6/7 - 4/5\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_str3(self):
        """
        Testing that proper str rep. is printed out when height is changed
        """

        self.obj = Rectangle(2, 5, 6, 7)
        result = "[Rectangle] (1) 6/7 - 2/5\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

        # Changing the value for height
        self.obj.height = 10
        result = result = "[Rectangle] (1) 6/7 - 2/10\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_str4(self):
        """
        Testing that proper str. rep. is printed out when x and y is changed
        """

        self.obj = Rectangle(2, 5, 6, 7)
        result = "[Rectangle] (1) 6/7 - 2/5\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

        # Changing the values of x and y
        self.obj.x = 4
        self.obj.y = 14
        result = "[Rectangle] (1) 4/14 - 2/5\n"

        with patch("sys.stdout", StringIO()) as str_out:
            print(self.obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_update(self):
        """
        Test updated attributes
        """

        self.obj = Rectangle(10, 10, 10, 10)
        result = "[Rectangle] (1) 10/10 - 10/10\n"

        with patch("sys.stdout", StringIO()) as upd_out:
            print(self.obj)
            self.assertEqual(upd_out.getvalue(), result)

        self.obj.update(89)
        result = "[Rectangle] (89) 10/10 - 10/10\n"
        with patch("sys.stdout", StringIO()) as upd_out:
            print(self.obj)
            self.assertEqual(upd_out.getvalue(), result)

        self.obj.update(89, 2, 3, 4, 5)
        result = "[Rectangle] (89) 4/5 - 2/3\n"
        with patch("sys.stdout", StringIO()) as upd_out:
            print(self.obj)
            self.assertEqual(upd_out.getvalue(), result)
