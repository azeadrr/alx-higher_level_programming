#!/usr/bin/python3
"""JSON string to Object"""

import json


def from_json_string(my_str):
    """Return: object representation of a JSON string"""
    return json.loads(my_str)
