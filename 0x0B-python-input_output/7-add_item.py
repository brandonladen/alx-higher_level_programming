#!/usr/bin/python3
"""Defines `add_item` module"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    lis = load_from_json_file("add_item.json")
except ValueError:
    lis = []
save_to_json_file(lis + sys.argv[1:], "add_item.json")
