#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    copy = a_dictionary.copy()
    sorted_arr = sorted(copy, key=lambda x: [ord(key) for key in x])
    for k in sorted_arr:
        print(f"{k}: {a_dictionary[k]}")
