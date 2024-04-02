#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_printed = 0
    for i in range(x):
        try:
            nb_printed += 1
            print(my_list[i], end='')
        except Exception:
            nb_printed = nb_printed - 1
            break
    print()
    return nb_printed
