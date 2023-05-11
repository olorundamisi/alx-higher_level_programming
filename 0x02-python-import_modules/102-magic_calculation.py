#!/usr/bin/python3
# 102-magic_calculation.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def magic_calculation(a, b):
    """Match ByteCode -> Python #3"""

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
