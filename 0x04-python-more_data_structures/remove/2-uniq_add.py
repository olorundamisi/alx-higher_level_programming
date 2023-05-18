#!/usr/bin/python3
# 2-uniq_add.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def uniq_add(my_list=[]):
    """Add all unique integers in a list."""

    result = 0

    uniq_list = set(my_list)
    for x in uniq_list:
        result += x

    return (result)
