#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5


def main():
    print("{} + {} = {}".format(10, 5, add(10, 5)))
    print("{} - {} = {}".format(10, 5, sub(10, 5)))
    print("{} * {} = {}".format(10, 5, mul(10, 5)))
    print("{} / {} = {}".format(10, 5, div(10, 5)))


if __name__ == "__main__":
    main()
