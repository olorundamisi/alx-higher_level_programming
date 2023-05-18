#!/usr/bin/python3
# 12-roman_to_int.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def roman_to_int(roman_string):
    """Convert a roman numeral to an arabic integer."""

    roman_str = roman_string

    if (not isinstance(roman_str, str) or roman_str is None):
        return (0)

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

    arabic_int = 0

    for i in range(len(roman_str)):
        if roman_dict.get(roman_str[i], 0) == 0:
            return (0)

        if (i != (len(roman_str) - 1) and
                roman_dict[roman_str[i]] < roman_dict[roman_str[i + 1]]):
                arabic_int += roman_dict[roman_str[i]] * -1
        else:
            arabic_int += roman_dict[roman_str[i]]

    return (arabic_int)
