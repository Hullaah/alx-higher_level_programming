#!/usr/bin/python3
"""This module contains the inherits_from function
done as part of the alx SE training
"""


def inherits_from(obj, a_class):
    """checks  if the object is an instance of a class that inherited (directl
    y or indirectly) from the specified class
    obj (object): object to be checked
    a_class (class): class
    Return: bool
    """
    return issubclass(type(obj), a_class) if type(obj) is not \
        a_class else False
