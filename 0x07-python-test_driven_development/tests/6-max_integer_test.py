"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Testing valid integers
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 6]), 6)
        self.assertEqual(max_integer([1, -2, 3]), 3)
        self.assertEqual(max_integer([-9, -3, -5, -1]), -1)

    def test_max_float(self):
        # Testing Float values
        self.assertEqual(max_integer([1.4, 2.0, 6.0]), 6)
        self.assertEqual(max_integer([-9.0, -3.4, -5.3, -1.0]), -1)

    def test_invalid_inputs(self):
        # Testing invalid types
        self.assertRaises(TypeError, max_integer, [1, [1,2,3], 4])
        self.assertRaises(TypeError, max_integer, [None, None, None])
    def test_strings(self):
        # Testing string input
        self.assertEqual(max_integer("Emmanuel"), 'u')
        self.assertEqual(max_integer("Ee"), 'e')
        self.assertEqual(max_integer("., (, *, !, )"), '.')

