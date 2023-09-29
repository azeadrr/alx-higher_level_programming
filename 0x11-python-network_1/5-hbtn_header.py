#!/usr/bin/python3
"""Python script that takes in a URL, sends
request to URL and displays value of
variable X-Request-Id"""

if __name__ == '__main__':
    import requests
    from sys import argv
    req = requests.get(argv[1])
    nes = req.headers.get('X-Request-Id')
    print(nes)
