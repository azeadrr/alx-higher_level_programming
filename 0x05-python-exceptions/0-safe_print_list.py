#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Returns the real number of elements printed
    """
    re = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            re += 1
        except IndexError:
            break
    print("")
    return (re)
