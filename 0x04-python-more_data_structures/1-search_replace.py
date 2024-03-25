#!/usr/bin/python3
"""def search_replace(my_list, search, replace):
    x = 0
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list"""

def search_replace(my_list, search, replace):
    def find_search(element):
        if element == search:
            return replace
        else:
            return element
    new_list = list(map(find_search, my_list))
    return(new_list)
