#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    df = 0

    for ty in my_list:
        number += ty[0] * ty[1]
        df += ty[1]

    return (number / df)
