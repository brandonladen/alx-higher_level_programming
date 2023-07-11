#!/usr/bin/python3
"""Defines `save_to_json_file` module"""
import json


def save_to_json_file(my_obj, filename):
    """
    returns the JSON representation of an object (string)
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
