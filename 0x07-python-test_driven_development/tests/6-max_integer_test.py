#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int_list(self):
        self.assertEqual(max_integer([2, 5, 6]), 6)
        self.assertEqual(max_integer([6, 5, 2]), 6)
        self.assertEqual(max_integer([2, 6, 5]), 6)
        self.assertEqual(max_integer([6]), 6)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_float_list(self):
        self.assertEqual(max_integer([2.2, 5.5, 6.6]), 6.6)
        self.assertEqual(max_integer([6.6, 5.5, 2.2]), 6.6)
        self.assertEqual(max_integer([2.2, 6.6, 5.5]), 6.6)

    def test_string_list(self):
        self.assertEqual(max_integer("Hello World"), 'r')
        self.assertEqual(max_integer(["Hello", "Hi"]), "Hi")
        self.assertEqual(max_integer(""), None)
        
