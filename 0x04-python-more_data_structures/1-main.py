#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [10, 1, 3, 2, 4, 5, 10, 11] # [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 10, 89)

print(new_list)
print(my_list)
