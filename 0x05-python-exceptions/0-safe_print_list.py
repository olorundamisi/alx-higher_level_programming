#!/usr/bin/python3
# 0-safe_print_list.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def safe_print_list(my_list=[], x=0):
    """Print `x` elememts of a list.

    Args:
        my_list (list): The list to print elements from.
          List elements could be of any type.
        x (int): The number of elements to print from my_list.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
