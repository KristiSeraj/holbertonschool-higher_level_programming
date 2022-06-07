#!/usr/bin/python3
"""Test module"""
import io, sys, unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_no_args(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_none_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_base(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_id_uniq(self):
        self.assertEqual(20, Base(20).id)
    
    def test_id_pub(self):
        base1 = Base(15)
        base1.id = 20
        self.assertEqual(20, base1.id)
