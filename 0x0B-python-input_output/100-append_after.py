#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line """


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing"""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
