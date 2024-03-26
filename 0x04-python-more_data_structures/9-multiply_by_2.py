#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_to_multiply = dict(a_dictionary)
    for keys in dict_to_multiply:
        dict_to_multiply.update({keys : (dict_to_multiply[keys] * 2)})
    return dict_to_multiply