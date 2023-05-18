#!/usr/bin/python3
# 12-roman_to_int.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def roman_to_int(roman_string):
    """Convert a roman numeral to an arabic integer."""

    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    rms = roman_string

    rmd = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 }

    arabic_int = 0

    for i in range(len(rms)):
        if (i != (len(rms) - 1) and rmd[rms[i]] < rmd[rms[i + 1]]):
            arabic_int += rmd[rms[i]] * -1
        else:
            arabic_int += rmd[rms[i]]

    return (arabic_int)
