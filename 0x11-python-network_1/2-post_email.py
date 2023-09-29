#!/usr/bin/python3
"""Python script that takes in URL and email,
sends a POST request to passed URL with email"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv
   
    url = argv[1]
    email = {'email': argv[2]}
    data = urlencode(email).encode('utf-8')
    requestrl = Request(url, data=data)
    with urlopen(requestrl) as res:
        nes = res.read().decode('utf-8')
        print(nes)
