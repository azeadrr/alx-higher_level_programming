#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square rectangle"""

    def __init__(self, size):
        """initialize new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
