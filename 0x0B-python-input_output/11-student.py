#!/usr/bin/python3
"""class Student that defines a student by: (based on 10-student.py)"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get a dictionary representation of student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes"""
        for k, v in json.items():
            setattr(self, k, v)
