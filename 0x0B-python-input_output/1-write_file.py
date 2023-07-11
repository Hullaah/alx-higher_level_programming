#!/usr/bin/python3
""" write file module
This module contains the write_file function done during
the alx SE course to demonstrate file I/O in python
"""


def write_file(filename="", text=""):
    """  writes a string to a text file (UTF8).
    Args:
        filename: name of file to be read
    Return:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as text_file:
        return text_file.write(text)
