#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char.isalpha():
            if 65 <= ord(char) <= 90:
            	pass
            else:
            	char = "{:c}".format(ord(char) - 97 + 65)
        print(char, end="")
    print()
