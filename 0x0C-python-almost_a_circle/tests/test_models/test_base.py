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

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_dict(self):
        self.assertEqual(str, type(Base.to_json_string([{'id': 12}])))

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_dict(self):
        self.assertEqual(list, type(Base.from_json_string('[{"id": 89}]')))

class TestBaseCreate(unittest.TestCase):
    def test_create_rectangle(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect_dict = rect.to_dictionary()
        rect2 = Rectangle.create(**rect_dict)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rect2))
