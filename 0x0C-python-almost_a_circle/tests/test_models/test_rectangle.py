#!/usr/bin/python3
"""Test module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleWidth(unittest.TestCase):
    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 2)

    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

if __name__ == '__main__':
    unittest.main()
