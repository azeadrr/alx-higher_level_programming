#!/usr/bin/python3
"""class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Args: name: name of parameter
              value: parameter to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
