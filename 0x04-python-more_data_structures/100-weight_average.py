#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    summation = 0
    frequency = 0
    for tup in my_list:
        summation += tup[0] * tup[1]
        frequency += tup[1]
    return summation / frequency
