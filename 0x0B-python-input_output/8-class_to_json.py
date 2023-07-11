#!/usr/bin/python3
"""function that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """return: a dictionary represntation of simple data structure"""
    return obj.__dict__
