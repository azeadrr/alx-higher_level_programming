#!/usr/bin/python3
"""Python script that takes in a URL, sends
a request to the URL and displays
the body of the response."""

if __name__ == '__main__':
    import requests
    from requests.exceptions import HTTPError
    from sys import argv
    req = requests.get(argv[1])
    if (req.status_code < 400):
        print(req._content.decode('utf-8'))
    else:
        print('Error code: {}'.format(req.status_code))
