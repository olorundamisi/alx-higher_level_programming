#!/usr/bin/python3
# 0-square_matrix_simple.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers in a matrix."""

    return ([list(map(lambda x: x * x, row)) for row in matrix])
