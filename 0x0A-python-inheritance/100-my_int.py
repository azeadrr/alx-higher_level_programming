#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """ MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """override == opeartor with !="""
        return self.real != value

    def __ne__(self, value):
        """override != operator with =="""
        return self.real == value
