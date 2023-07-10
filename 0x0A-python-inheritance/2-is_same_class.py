#!/usr/bin/python3
"""This is the module for 2-is_same_class file done
diuring the alx SE course
"""


def is_same_class(obj, a_class):
    """checks  if the object is exactly an instance of the specified class
    obj (object): object to be checked
    a_class (class): class to check for instance existence
    Return: bool
    """
    return type(obj) is a_class
