#!/usr/bin/python3
""" read json file"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”:"""
    with open(filename) as f:
        return json.load(f)
