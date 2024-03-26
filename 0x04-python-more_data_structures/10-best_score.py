#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    list_value = a_dictionary.values()
    x = 0
    for i in list_value:
        if i > x:
            x = i
    for key in a_dictionary:
        if a_dictionary[key] == x:
            return key
