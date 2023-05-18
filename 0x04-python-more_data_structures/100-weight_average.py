#!/usr/bin/python3
# 100-weight_average.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def weight_average(my_list=[]):
    """Return the weighted average of all the integers in a list of
    tuples (<score>, <weight>)."""

    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    sw_sum = 0
    wt_sum = 0

    for tup in my_list:
        sw_sum += (tup[0] * tup[1])
        wt_sum += tup[1]

    return (sw_sum / wt_sum)
