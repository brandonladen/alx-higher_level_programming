#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_def(self):
        """test normal input"""
        self.assertEqual(max_integer([2,3,7,5,2]), 7)

    def test_none(self):
        """tests empty input"""
        self.assertEqual(max_integer(), None)

    def test_neg(self):
        """tests negative"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_neg_pos(self):
        """tests composed input"""
        self.assertEqual(max_integer([1, -4, -5, 5, 3]), 5)

    def test_non_int(self):
        """tests with non integer input"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

    def test_float(self):
        """tests with float"""
        self.assertEqual(max_integer([1, 2, 3.3]), 3.3)

if __name__ == "__main__":
    unittest.main()
