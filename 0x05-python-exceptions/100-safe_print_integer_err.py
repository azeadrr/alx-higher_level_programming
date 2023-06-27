#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    "{:d}".format() to print as integer
    value: The integer
    Returns: True if value has been correctly printed,
    Otherwise, returns False and prints in stderr the error precede by Exception
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
