#!/usr/bin/python3
def no_c(my_string):
    c = "cC"
    string = ""
    for letter in my_string:
        if letter not in c:
            string += letter
    return string
