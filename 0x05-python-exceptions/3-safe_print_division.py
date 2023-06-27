#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the value of the division, otherwise"""
    try:
        divi = a / b
    except (TypeError, ZeroDivisionError):
        divi = None
    finally:
        print("Inside result: {}".format(divi))
    return (divi)
