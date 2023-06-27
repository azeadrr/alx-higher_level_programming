#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    x represents the number of elements to print
    Prints x elememts of a list.
    Return: The number of elements printed.
    """
    l = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            l += 1
        except IndexError:
            break
    print("")
    return (l)
