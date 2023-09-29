#!/usr/bin/python3
"""Python script that takes
your GitHub credentials"""

if __name__ == '__main__':
    from sys import argv
    from requests import get
    from requests.auth import HTTPBasicAuth
    tkn = argv[2]
    usr = argv[1]
    login = HTTPBasicAuth(usr, tkn)

    reqs = get('https://api.github.com/user', auth=login)
    json = reqs.json()
    print(json.get('id'))
