#!/usr/bin/python3
"""Defines a student"""


class Student:
    """Student class

    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Initialize a student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a disctionary representation of a Student"""

        return self.__dict__
