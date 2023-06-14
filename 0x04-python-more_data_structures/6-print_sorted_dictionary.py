#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        copy = a_dictionary.copy()
        sorted(copy,key=lambda x: [ord(key) for key in x])
        for k, v in copy.items():
            print(f"{k}: {v}")
    
