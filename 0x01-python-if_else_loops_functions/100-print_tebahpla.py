#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:c}".format(i if not i % 2 else i - 32), end="")
