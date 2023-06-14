#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    status = 0
    largest = 0
    for k, v in a_dictionary.items():
        if not status:
            largest = v
            name = k
            status = 1
            continue
        if v > largest:
            largest = v
            name = k
    return name
