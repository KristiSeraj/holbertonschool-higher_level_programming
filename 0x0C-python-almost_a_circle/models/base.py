#!/usr/bin/python3
"""Defines a base module"""


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
