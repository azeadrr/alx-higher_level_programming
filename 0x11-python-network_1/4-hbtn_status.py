#!/usr/bin/python3
"""Python script that fetches
https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(req.content.decode('utf-8'))))
    print('\t- content: {}'.format(req.content.decode('utf-8')))
