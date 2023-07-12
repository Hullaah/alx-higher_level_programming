#!/usr/bin/python3
""" stats module
This module contains a script that reads stdin line
by line and computes metrics done during the alx SE
used to demonstrate file I/O in python
"""


import sys


def main():
    first = 1
    if first:
        first = 0
        lines_read = sys.stdin.readlines(10)
        status_codes = []
        file_size = 0
        for line in lines_read:
            line_arr = line.split()
            status_codes.append(line_arr[6])
            file_size += int(line_arr[7])
        print("File size:", file_size)
        for x in 


