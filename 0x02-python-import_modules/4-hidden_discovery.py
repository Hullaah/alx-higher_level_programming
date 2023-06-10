#!/usr/bin/python3
import hidden_4


def main():
    for elem in dir(hidden_4):
        if elem[:2] != "__":
            print(elem)


if __name__ == "__main__":
    main()
