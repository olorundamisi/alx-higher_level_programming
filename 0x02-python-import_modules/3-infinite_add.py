#!/usr/bin/python3
# 3-infinite_add.py
# Olorundamisi Dunmade <github.com/olorundamisi>


if __name__ == "__main__":
    """Print the addition of all arguments."""

    import sys

    sum_total = 0
    for i in range(len(sys.argv) - 1):
        sum_total += int(sys.argv[i + 1])

    print("{}".format(sum_total))
