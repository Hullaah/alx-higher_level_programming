#!/usr/bin/python3
""" append write module
This module contains the append_write function done during
the alx SE course to demonstrate file I/O in python
"""


def append_write(filename="", text=""):
    """  writes a string to a text file (UTF8).
    Args:
        filename: name of file to be read
    Return:
        Number of characters written
    """
    with open(filename, "a", encoding="utf-8") as text_file:
        return text_file.write(text)
