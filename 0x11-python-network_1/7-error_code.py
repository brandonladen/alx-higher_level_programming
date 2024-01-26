#!/usr/bin/python3
"""If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code:', r.status_code)
