#!/usr/bin/python3
""" function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
	return: the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
