#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get a dictionary representation of Student"""
        return self.__dict__
