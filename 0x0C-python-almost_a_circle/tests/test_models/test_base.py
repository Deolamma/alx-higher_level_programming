#!/usr/bin/python3
"""
unittest file for Base(id)
"""
import unittest
from models.base import Base


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
        self.obj1 = Base()
        self.obj2 = Base()
        self.obj3 = Base(8)
        self.obj4 = Base()
        self.obj5 = Base([1, 2, "emmanuel", {"name": "e", "id": 10}])
        self.obj6 = Base(-7)
        self.obj7 = Base()

    def tearDown(self):
        """tears down after tests
        """

        print("teardown")
 
    def test_init_id_none(self):
        """tests for if id is none
        """

        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj4.id, 3)
        self.assertEqual(self.obj7.id, 4)

    def test_init_id_value(self):
        """tests for if id has a value
        """

        self.assertEqual(self.obj3.id, 8)
        self.assertEqual(self.obj6.id, -7)
        self.assertEqual(self.obj5.id, [1, 2, "emmanuel", {"name": "e", "id": 10}])
