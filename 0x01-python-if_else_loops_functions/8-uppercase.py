#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if isalpha(char):
            if 65 <= ord(char) <= 90:
                print(char, end="")
            else:
                print("{:c}".format(ord(char) - 97 + 65))
