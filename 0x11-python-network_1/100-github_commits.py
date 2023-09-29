#!/usr/bin/python3
"""Python script that takes 2 arguments
in order to solve this challenge."""

if __name__ == '__main__':
    from sys import argv
    from requests import get
    rpo = argv[1]
    own = argv[2]

    reqs = get('https://api.github.com/repos/{}/{}/commits'
                  .format(own, rpo))
    json = reqs.json()

    try:
        for i in range(10):
            hr = json[i].get('hr')
            name = json[i].get('commit').get('author').get('name')
            print("{}: {}".format(hr, name))
    except IndexError:
        pass
