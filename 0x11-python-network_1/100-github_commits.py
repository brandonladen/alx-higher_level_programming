#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    j = r.json()
    try:
        for i in range(10):
            print(j[i].get('sha'), j[i].get('commit')
                  .get('author').get('name'), sep=": ")
    except:
        pass
