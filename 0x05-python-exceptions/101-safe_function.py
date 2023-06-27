#!/usr/bin/python3

import sys
def safe_function(fct, *args):
    """
    fct: a pointer to a function
    args: the arguments for fct.
    Returns: if something happens during the function and prints in stderr the error precede by Exception
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
