#!/usr/bin/python3
def find(my_list, x):
    if not my_list or x not in my_list:
        return
    for i in range(len(my_list)):
        if my_list[i] == x:
            return i


def search_replace(my_list, search, replace):
    copy = my_list[:]
    exist = search in copy
    while exist:
        index = find(copy, search)
        copy[index] = replace
        exist = search in copy
    return copy
