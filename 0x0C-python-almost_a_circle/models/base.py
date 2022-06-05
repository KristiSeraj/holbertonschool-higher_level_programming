#!/usr/bin/python3
"""Defines a base module"""
import json


class Base:
    """Base class

    Attribute:
        __nb_objects (int): number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ initialize base class

        Args:
            id (int): id of object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a filei"""

        new_list = []
        new_file = cls.__name__ + ".json"
        if new_list is not None:
            for el in list_objs:
                new_list.append(el.to_dictionary())
        with open(new_file, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(new_list))
