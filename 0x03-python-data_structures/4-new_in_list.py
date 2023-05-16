#!/usr/bin/python3
# 4-new_in_list.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position. But
    return a copy and leave the original list as is.
    """

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = element

    return (copy)
