#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square class module

This module is part of the project done during the alx SE course.
It contains a Square class object that stores a private size attribute.

"""


class Square:
    """The Square class object.

        It is a class that stores a private size
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): The size of the square
        Attributes:
            _size (int): private size attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= to 0")
        self.__size = size
