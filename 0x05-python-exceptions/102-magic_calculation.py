#!/usr/bin/python3
# 102-magic_calculation.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += ((a ** b) / i)
        except Exception as error:
            result = b + a
            break
    return (result)
