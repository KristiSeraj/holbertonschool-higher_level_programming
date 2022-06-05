"README.md" 27L, 1904C                                                                                27,142        Bot
# Inheritance

- [tests](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/tree/main/0x0A-python-inheritance/tests) - Directory containing test files for Python scripts

- [0-lookup.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/0-lookup.py) - Python script that returns the list of available attributes and methods of an object.

- [1-my_list.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/1-my_list.py) - Python script that has a class `MyList` which inherits from `list` with: 
   - public instance method `def print_sorted(self):` that prints the list, but sorted(ascending sort)

- [10-square.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/10-square.py) - Python script with class `Square` that inherits from `Rectangle`
  - Instantiation with `size`: `def __init__(self, size):`
    - `size` is private: No getter or setter
    - `size` is positive integer, validated by `integer_validator`
  - the `area()` method is implemented

- [11-square.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/11-square.py) - Python script with class `Square` that inherits from `Rectangle`
  - Instantiation with `size`: `def __init__(self, size):`
    - `size` is private: No getter or setter
    - `size` is positive integer, validated by `integer_validator`
  - the `area()` method is implemented
  - `print()` prints, `str()` returns, the square description: `[Square] <width>/<height>`

- [2-is_same_class.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/2-is_same_class.py) - Python script that returns `True` if the object is *exactly* an instance of the specific class, otherwise `False`

- [3-is_kind_of_class.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/3-is_kind_of_class.py) - Python script that returns `True` if the object is an instance of, or if the objects is an instance of a class that inherited from, the specific class, otherwise returns `False`

- [4-inherits_from.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/4-inherits_from.py) - Python script that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class, otherwise returns `False`

- [5-base_geometry.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/5-base_geometry.py) - Python script with an empty class `BaseGeometry`

- [6-base_geometry.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/6-base_geometry.py) - Python script with class `BaseGeometry`:
   - public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`

- [7-base_geometry.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py) - Python script with class `BaseGeometry`:
   - public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
   - public instance method: `def integer_validator(self, name, value):` that validates `value`
     - `name` is always a string
     - if `value` is not an integer: raises a `TypeError` exception, with the message `<name> must be an integer`
     - if `value` is less or equal to 0: raises a `ValueError` exception with the message `<name> must be greater that 0`

- [8-rectangle.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/8-rectangle.py) - Python script with class `Rectangle` that inherits from `BaseGeometry`
  - Instantiation with `width` and `height`: `def __init__(self, width, height):`
    - `width` and `height` are private: No getter or setter
    - `width` and `height` are positive integers, validated by `integer_validator`

- [9-rectangle.py](https://github.com/KristiSeraj/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/9-rectangle.py) - Python script with class `Rectangle` that inherits from `BaseGeometry`
  - Instantiation with `width` and `height`: `def __init__(self, width, height):`
    - `width` and `height` are private: No getter or setter
    - `width` and `height` are positive integers, validated by `integer_validator`
  - the `area()` method is implemented
  - `print()` prints, and `str()` returns, the following rectangle description: `[Rectangle] <width>/<height>`
