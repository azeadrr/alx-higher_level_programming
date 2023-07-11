#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """built-in list class"""

    def print_sorted(self):
        """print a list ascending"""
        print(sorted(self))
