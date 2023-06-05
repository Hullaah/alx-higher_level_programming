#!/usr/bin/python3
import os
from sys import exit
word = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
os.write(2, bytes(word, "utf-8"))
exit(1)
