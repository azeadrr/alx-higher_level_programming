#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """
        size: The integer value of size of new square
        """
        self.size = size

    @property
    def size(self):
        """set size of the square"""
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
