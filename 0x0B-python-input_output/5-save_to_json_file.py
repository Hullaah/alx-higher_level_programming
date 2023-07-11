#!/usr/bin/python3
"""save to json file module
This module contains the save_to_json_file module
used to demonstrate file I/O and the json library in
python
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to be converted to json string
        filename: name of file which my_obj json representation
                is to be written
    Return:
        None
    """
    with open(filename, "w", encoding="utf-8") as text_file:
        json.dump(my_obj, text_file)
