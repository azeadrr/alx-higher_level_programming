#!/usr/bin/python3
"""Python script that takes in a URL and an
email address sends a POST request to
passed URL with the email"""

if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    email = {'email': argv[2]}
    req = requests.post(url, data=email)
    nes = req._content.decode('utf-8')
    print(nes)
