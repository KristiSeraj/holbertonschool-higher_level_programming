#!/usr/bin/python3
"""Square class that prints a square"""


class Square:
    """__init__method that initialize a square class
    Args:
        size: size of square
        position: position of square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the instance attribute for size"""

        return self.__size

    @property
    def position(self):
        """Retrieves the instance attribute for position"""

        return self.__position

    @size.setter
    def size(self, value):
        """Sets value to size and checks for errors"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Checks for erros for position and sets value to position"""

        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
                or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of square
        Return:
            returns the area of the square
        """

        return self.size * self.size

    def my_print(self):
        """Prints the square based on the size with '#' """

        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for row in range(self.__size):
                print(" " * self.position[0], end="")
                for col in range(self.__size):
                    print("#", end="")
                print("")
