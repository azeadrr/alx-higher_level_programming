#!/usr/bin/python3
"""Python script that takes in URL
sends request to URL and displays body"""

if __name__ == '__main__':
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

    try:
        with urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as er:
        print('Error code: {}'.format(er.code))
