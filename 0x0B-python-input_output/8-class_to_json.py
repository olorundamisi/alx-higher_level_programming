#!/usr/bin/python3
# 8-class_to_json.py
# Olorundamisi Dunmade <github.com/olorundamisi>
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
