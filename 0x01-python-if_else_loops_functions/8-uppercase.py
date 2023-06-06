#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 65 <= ord(char) <= 90:
            print(char, end="")
