#!/usr/bin/python3
import sys


def main():
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("0 arguments.")
    elif arg_len == 2:
        print("1 argument:")
    else:
        print(arg_len - 1, "arguments:")
    i = 1
    while i < arg_len:
        print("{}:".format(i), sys.argv[i])
        i += 1


if __name__ == "__main__":
    main()
