#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = find(a_dictionary, value)
    if not keys:
        pass
    else:
        for elem in keys:
            del a_dictionary[elem]
    return a_dictionary


def find(a_dictionary, value):
    ret = []
    for k, v in a_dictionary.items():
        if v == value:
            ret.append(k)
    if not ret:
        return None
    return ret
