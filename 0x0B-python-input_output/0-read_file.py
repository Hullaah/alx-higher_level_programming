#!/usr/bin/python3
""" read file module
This module contains the read_file function done during
the alx SE course to demonstrate file I/O in python
"""


def read_file(filename: str = ""):
    """ reads a text file (UTF8) and prints it to stdout.
    Args:
        filename: name of file to be read
    Return:
        None
    """
    with open(filename, encoding="utf-8") as text_file:
        print(text_file.read())
