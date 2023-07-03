#!/usr/bin/python3
"""add_integer module

This module contains the add_integer function. It was created
during the alx SE sponsored programme. It was created to practice
and demonstrate testing with python doctest library
"""


def add_integer(a, b=98):
    """
    Descrption: adds two numbers together
    Args:
        a (number): first number
        b (number): second number
    Return: integer sum of a and b
    Raises:
        TypeError: if a is not a number or b is not a number
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
