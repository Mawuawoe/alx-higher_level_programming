#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide elements of my_list_1 by elements of my_list_2 element
    -wise up to a specified length.
    Args:
    my_list_1 (list): The first list.
    my_list_2 (list): The second list.
    list_length (int): The length up to which elements should be divided.
    Returns:
    list: A new list containing the result of element-wise division.
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        new_list.append(result)
    return new_list
