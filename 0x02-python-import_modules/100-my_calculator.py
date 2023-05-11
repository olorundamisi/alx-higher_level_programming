#!/usr/bin/python3
# 100-my_calculator.py
# Olorundamisi Dunmade <github.com/olorundamisi>


if __name__ == "__main__":
    """Handle basic arithmetic operations."""

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op_dict = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(op_dict.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b, op_dict[sys.argv[2]](a, b)))
