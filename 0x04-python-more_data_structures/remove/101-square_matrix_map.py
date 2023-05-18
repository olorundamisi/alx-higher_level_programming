#!/usr/bin/python3
# 101-square_matrix_map.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def square_matrix_map(matrix=[]):
    """Compute the square value of all integers of a matrix using 'map'."""

    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
