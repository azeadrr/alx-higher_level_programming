#!/usr/bin/python3

"Print numbers from 0 to 98 in hexadecimal and decimal."
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
