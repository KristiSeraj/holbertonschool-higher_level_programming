#!/usr/bin/python3
"""Square class that access and update private attribute"""


class Square:
    """__init__method that initialize a square class
    Args:
        size: size of square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieves the instance attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets value to size and checks for errors"""

        if type(value) != int:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of square
        Return:
            returns the area of the square
        """

        return self.__size * self.__size

    def __eq__(self, other):
        """Compares object self to other and
        returns True if objects are equal"""

        return self.area() == other.area()

    def __ne__(self, other):
        """Compares object self to other and
        returns True if objects are not equal"""

        return self.area() != other.area()

    def __lt__(self, other):
        """Compares object self to other and
        returns True if current is less than other"""

        return self.area() < other.area()

    def __gt__(self, other):
        """Compares object self to other and
        returns True if current is great than other"""

        return self.area() > other.area()

    def __le__(self, other):
        """Compares object self to other and
        returns True if current is less equal than other"""

        return self.area() <= other.area()

    def __ge__(self, other):
        """Compares object self to other and
        returns True if current is great equal than other"""

        return self.area() >= other.area()
