#!/usr/bin/python3
"""load from json file module
This module contains the from_json_string function used to convert
json to python object{"is_active": true, 12 }
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
        filename: object to be converted to json string
    Return: object
    """
    with open(filename, encoding="utf-8") as text_file:
        return json.load(text_file)
