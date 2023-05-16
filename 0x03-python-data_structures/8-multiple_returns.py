#!/usr/bin/python3
# 8-multiple_returns.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def multiple_returns(sentence):
    """Return the length of a string and its first character."""

    if sentence == "":
        return (0, None)

    return (len(sentence), sentence[0])
