#!/usr/bin/python3


def safe_print_integer(value):
    """
    "{:d}".format() to print as integer
    value: The integer
    Returns: True if value has been correctly printed, Otherwise, returns False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
