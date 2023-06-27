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
    def __init__(self, size):
        """
        Args:
            size (int): The size of the square
        Attributes:
            _size (int): private size attribute
        """
        self.__size = size
