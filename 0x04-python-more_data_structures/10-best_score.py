#!/usr/bin/python3
# 10-best_score.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def best_score(a_dictionary):
    """Return a key with the largest integer value."""

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    max_key = list(a_dictionary.keys())[0]
    max_val = a_dictionary[max_key]

    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            max_key = k

    return (max_key)
