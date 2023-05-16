#!/usr/bin/python3
# 5-no_c.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def no_c(my_string):
    """Remove all characters c and C from a string."""

    copy = [_ for _ in my_string if _ != 'c' and _ != 'C']

    return ("".join(copy))
