#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """
        size: The integer value of size of new square
        """
        self.size = size

    @property
    def size(self):
        """set size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """== comparision to Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """!= comparison to Square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """< comparison to Square"""
        return self.area() < other.area()

    def __le__(self, other):
        """<= comparison to Square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """> comparison to Square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= compmarison to Square"""
        return self.area() >= other.area()
