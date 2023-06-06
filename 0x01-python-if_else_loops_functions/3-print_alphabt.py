#!/usr/bin/python3
for i in range(97, 123):
    if "{:c}".format(i) != "q" and "{:c}".format(i) != "e":
        print("{:c}".format(i), end="")