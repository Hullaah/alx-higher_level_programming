#!/usr/bin/python3
"""This module contains the is_kind_of_class function
done as part of the alx SE training
"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
    obj (object): object to be checked
    a_class (class): class
    Return: bool
    """
    return isinstance(obj, a_class)
