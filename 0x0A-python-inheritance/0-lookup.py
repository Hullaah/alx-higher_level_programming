#!/usr/bin/python3
"""This module contains the lookup function
It contains the lookup function that returns a list of all methods
of a class
"""


def lookup(obj):
    """Returns the list of methods of an object
    obj (class): object
    Returns: list of object methods
    """
    return dir(obj)
