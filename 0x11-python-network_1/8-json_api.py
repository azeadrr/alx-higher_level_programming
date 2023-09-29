#!/usr/bin/python3
""" Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user"""

if __name__ == '__main__':
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) != 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    req = requests.post(url, data=data)

    try:
        json = req.json()
        if json != {}:
            print('[{}] {}'.format(json.get("id"), json.get("name")))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
