#!/usr/bin/python3
# 9-max_integer.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def max_integer(my_list=[]):
    """Find the largest integer in a list."""
    
    if len(my_list) == 0:
        return (None)

    largest = my_list[0]

    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    return (largest)
