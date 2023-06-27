#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """
        size: The integer value of  size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size