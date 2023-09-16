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

    def tearDown(self):
        """tears down after tests
        """

        print("teardown")

    def test_init_id_none(self):
        """tests for if id is none
        """

        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        obj3 = Base()
        obj4 = Base()
        self.assertEqual(obj4.id, 4)

    def test_init_id_value(self):
        """tests for if id has a value
        """

        obj1 = Base(8)
        self.assertEqual(obj1.id, 8)
        obj2 = Base(-7)
        self.assertEqual(obj2.id, -7)
        obj3 = Base([1, 2, "emmanuel", {"name": "e", "id": 10}])
        self.assertEqual(obj3.id, [1, 2, "emmanuel", {"name": "e", "id": 10}])

    if __name__ == '__main__':
        unittest.main()
