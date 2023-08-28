#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list.

    Args:
        my_list (list): Contain any data type.
        x (int): represents the number of elements to print.

    Returns:
        The real number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
