#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with email as parameter"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode

    url = argv[1]
    requestrl = Request(url, data=data)
    email = {'email': argv[2]}
    data = urlencode(email).encode('utf-8')
    with urlopen(requestrl) as res:
        nes = res.read().decode('utf-8')
        print(nes)
