#!/usr/bin/python3
"""Print string"""


def say_my_name(first_name, last_name=""):
    """Print my name is <first_name> <last_name>

    Args:
        first_name (str): first name
        last_name (str): last name
    Raises:
        raise TypeError if first_name and last_name are not strings
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
