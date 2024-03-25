#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = 0
    new_list = my_list[:]
    for i in new_list:
        if i == search:
            break
        else:
            x = x + 1
    new_list[x] = replace
    return new_list
