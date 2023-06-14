#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lst_keys = list(a_dictionary.keys())

    for value_of_dict in lst_keys:
        if value == a_dictionary.get(value_of_dict):
            del a_dictionary[value_of_dict]

    return (a_dictionary)
