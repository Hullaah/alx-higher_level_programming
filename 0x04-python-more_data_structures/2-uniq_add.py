#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    ans = 0
    for elem in my_set:
        ans += elem
    return ans
