#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    if __name__ == '__main__':
        with urlopen(argv[1]) as res:
            nes = res.headers.get('X-Request-Id')
            print(nes)
