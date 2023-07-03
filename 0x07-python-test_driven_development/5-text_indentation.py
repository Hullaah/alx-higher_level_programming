#!/usr/bin/python3
"""text_indentation module

This module contains the text_indentation function. It was created
during the alx SE sponsored programme. It was created to practice
and demonstrate testing with python doctest library
"""


def text_indentation(text: str):
    """
    Description: prints a text with 2 new lines after each of these
    characters: ., ? and : removing any space at the beginning of the newline
    Args:
        text: the text to be printed
    Return: None
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    string = ".:?"
    i = 0
    string_arr = []
    while i < len(text):
        if text[i] in string:
            string_arr.append(text[i])
            string_arr.extend("\n\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        else:
            string_arr.append(text[i])
        i += 1
    print("".join(string_arr), end="")
