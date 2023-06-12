#!/usr/bin/python3
# 1-my_list.py
# Olorundamisi Dunmade <github.com/olorundamisi>
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list sorted in non-decreasing/ascending order."""
        print(sorted(self))
