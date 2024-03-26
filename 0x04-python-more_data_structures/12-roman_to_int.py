#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_v = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_n[roman_string[i]] > roman_n[roman_string[i - 1]]:
            integer_v = roman_n[roman_string[i]] - roman_n[roman_string[i - 1]]
        else:
            integer_v = integer_v + roman_n[roman_string[i]]
    return integer_v
