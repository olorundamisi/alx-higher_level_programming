#!/usr/bin/python3
# 12-roman_to_int.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def roman_to_int(roman_string):
    """Convert a roman numeral to an arabic integer."""

    if (not isinstance(roman_string, str) or roman_string is None):
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

    for i in range(len(roman_string)):
        if roman_dict.get(roman_string[i], 0) == 0:
            return (0)

        neg = roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]
        if (i != (len(roman_string) - 1) and neg):
            arabic_int += roman_dict[roman_string[i]] * -1
        else:
            arabic_int += roman_dict[roman_string[i]]

    return (arabic_int)
