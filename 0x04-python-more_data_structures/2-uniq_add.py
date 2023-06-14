#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return
    my_set = set(my_list)
    ans = 0
    for elem in my_set:
        ans += elem
    return ans
