#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_alphabetically = sorted(a_dictionary.keys())
    for keys in sorted_alphabetically:
        print("{}: {}". format(keys, a_dictionary[keys]))
