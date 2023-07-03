#!/usr/bin/python3
"""say_my_name module

This module contains the say_my_name function. It was created
during the alx SE sponsored programme. It was created to practice
and demonstrate testing with python doctest library
"""


def say_my_name(first_name: str, last_name: str = "") -> None:
    """
    Description: prints the formatted name of a person
    Args:
        first_name: person's first name
        last_name: person's last_name
    Return:
        None
    Raises:
        TypeError: if first_name or last_name is not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
