#!/usr/bin/python3
"""class MagicClass that does exactly the same as the following Python"""

import math


class MagicClass:
    """class circle"""

    def __init__(self, radius=0):
        """
        radius: a radius of new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius number")
        self.__radius = radius

    def area(self):
        """Return area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return circumference"""
        return (2 * math.pi * self.__radius)
