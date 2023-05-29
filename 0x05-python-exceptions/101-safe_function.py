#!/usr/bin/python3
# 101-safe_function.py
# Olorundamisi Dunmade <github.com/olorundamisi>

import sys


def safe_function(fct, *args):
    """Execute a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)