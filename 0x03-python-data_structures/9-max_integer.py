#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    status = 0
    largest = 0
    for val in my_list:
        if not status:
            largest = val
            status = 1
            continue
        if val > largest:
            largest = val
    return largest
