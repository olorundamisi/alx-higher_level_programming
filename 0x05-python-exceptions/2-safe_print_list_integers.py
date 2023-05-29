#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def safe_print_list_integers(my_list=[], x=0):
    """Print the first `x` elements of a list that are integers.

    Items in the list that are unable to be printed such as non-integers
    will be skipped (in silence).

    Args:
        my_list (list): The list to print elements from.
          List elements could be of any type.
        x (int): The number of elements to print from my_list.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
