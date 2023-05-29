#!/usr/bin/python3
# 4-list_division.py
# Olorundamisi Dunmade <github.com/olorundamisi>


def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element.

    Args:
        my_list_1 (list): The dividend list.
        my_list_2 (list): The divisor list.
        list_length (int): The number of elements to divide. The length of
          both lists

    Returns:
        new_list (list): The quotient list.
          A list of length list_length containing all the resulting quotients.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
