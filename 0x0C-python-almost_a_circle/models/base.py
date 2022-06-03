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

        if list_objs is None:
            list_objs = []

