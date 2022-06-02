#!/usr/bin/python3
"""Rectangle module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize rectangle class"""

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter function"""

        return self.width

    @size.setter
    def size(self, size):
        """Setter function"""

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""

        args_list = ["id", "size", "x", "y"]

        if args and len(args) != 0:
            for a_el in range(len(args)):
                setattr(self, args_list[a_el], args[a_el])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """Str representation of square"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
