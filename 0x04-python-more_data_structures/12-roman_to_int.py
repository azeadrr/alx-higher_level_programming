#!/usr/bin/python3
def to_subtract(lst_num):
    sub = 0
    max_lst = max(lst_num)

    for n in lst_num:
        if max_lst > n:
            sub += n

    return (max_lst - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_nu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lst_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    lst_num = [0]

    for ch in roman_string:
        for re_num in lst_keys:
            if re_num == ch:
                if rom_nu.get(ch) <= last_rom:
                    num += to_subtract(lst_num)
                    lst_num = [rom_nu.get(ch)]
                else:
                    lst_num.append(rom_nu.get(ch))

                last_rom = rom_nu.get(ch)

    num += to_subtract(lst_num)

    return (num)
