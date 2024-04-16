#!/usr/bin/python3
# 2-is_same_class.py
# Olorundamisi Dunmade <github.com/olorundamisi>
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """ Returns True if object is instance of class ;
    otherwise False.
    Args:
        obj -> the object in question
        a_class -> the class to compared against
    Returns:
        True if type(obj) == a_class; False otherwise
    """
    return isinstance(obj, a_class) and type(obj) == a_class
