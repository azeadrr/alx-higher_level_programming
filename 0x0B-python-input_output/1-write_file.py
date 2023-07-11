#!/usr/bin/python3
""" writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """
    Return: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
