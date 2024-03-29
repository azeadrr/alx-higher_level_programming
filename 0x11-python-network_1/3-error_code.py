#!/usr/bin/python3
"""Python script that takes in URL
sends request to URL and displays body"""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as res:
            nes = res.read().decode('utf-8')
            print(nes)
    except HTTPError as er:
        print('Error code: {}'.format(er.code))
