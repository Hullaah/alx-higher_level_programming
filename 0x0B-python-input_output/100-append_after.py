#!/usr/bin/python3
""" append after module
This module contains the append_after function
done during the alx SE used to demonstrate file I/O
in python
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing a
    specific string
    Args:
        filename: name of file to append to
        search_string: string to append after
        new_string: string to be appended
    Return:
        None
    """
    written = ""
    with open(filename, "r+", encoding="utf-8") as text_file:
        for line in text_file:
            if search_string in line:
                written += line + new_string
            else:
                written += line
    with open(filename, "w", encoding="utf-8") as text_file:
        text_file.write(written)
