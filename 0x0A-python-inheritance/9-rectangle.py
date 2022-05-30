#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines a module"""


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Return the following rectangle description"""

        return f"[Rectangle] {self.__width}/{self.__height}"
