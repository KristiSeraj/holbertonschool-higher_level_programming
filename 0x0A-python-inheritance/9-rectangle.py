#!/usr/bin/python3
"""Defines a module"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Raises an exception error"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name (str): string
            value (int): integer
        Raise:
            raises TypeError if value is not int and
            ValueError if value is less or equal to 0
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

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
