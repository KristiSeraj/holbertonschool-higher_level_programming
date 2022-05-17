#!/usr/bin/python3
"""Square class that prints a square"""


class Square:
    """__init__method that initialize a square class
    Args:
        size: size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the instance attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets value to size and checks for errors"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the instance attribute for position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Checks for erros for position and sets value to position"""

        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of square
        Return:
            returns the area of the square
        """

        return self.__size * self.__size

    def my_print(self):
        """Prints the square based on the size with '#' """

        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
