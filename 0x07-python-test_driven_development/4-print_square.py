#!/usr/bin/python3
"""print_square module

This module contains the print_square function. It was created
during the alx SE sponsored programme. It was created to practice
and demonstrate testing with python doctest library
"""


def print_square(size: int):
    """
    Description: prints a square of size denoted by size
    Args:
        size: size of square to be printed
    Return: None
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not size:
        print()
    for i in range(size):
        print("#" * size)
