#!/usr/bin/python3
import sys
def main():
    arg_len = len(sys.argv)
    i = 1
    ans = 0
    while i < arg_len:
        ans += int(sys.argv[i])
        i += 1
    print("{}".format(ans))
if __name__ == "__main__":
    main()
