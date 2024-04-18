#!/usr/bin/python3
"""
This module  prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Arg:
        text: text  must be a string, otherwise raise a TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation_marks = ['.', '?', ':']
    skip_space = False
    first_char_of_line = True
    for char in text:
        if skip_space and char == ' ':
            continue
        if first_char_of_line and char == ' ':
            continue
        print(char, end='')
        first_char_of_line = False
        skip_space = False
        if char in punctuation_marks:
            skip_space = True
            print('\n\n', end='')
        if char == '\n':
            first_char_of_line = True
