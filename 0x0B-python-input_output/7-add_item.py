#!/usr/bin/python3
"""add item module
This module contains a script that adds all arguments
supplied at the command-line to a list and then save them to a file.
It was used to demonstrate file I/O and the python json standard library
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """Entry point for the script
    Args:
        Empty (no args)
    Return:
        None
    """
    arg_list = []
    json_file = open("add_item.json", "a", encoding="utf-8")
    for i in range(1, len(sys.argv)):
        arg_list.append(sys.argv[i])
    if json_file.tell():
        json_file.close()
        arg_list = load_from_json_file("add_item.json") + arg_list
    json_file.close()
    save_to_json_file(arg_list, "add_item.json")


if __name__ == "__main__":
    main()
