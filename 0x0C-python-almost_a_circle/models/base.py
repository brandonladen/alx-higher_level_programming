#!/usr/bin/python3
"""Defines base model"""
import json


class Base:
    """
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns A JSON STRING
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes JSON string representation of list_objs to a file
        """
        d = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as myFile:
            if list_objs:
                for obj in list_objs:
                    d.append(obj.to_dictionary())
            myFile.write(cls.to_json_string(d))

    @staticmethod
    def from_json_string(json_string):
        """
            write json representation of string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        """
        if cls.__name__ == 'Rectangle':
            a = cls(1, 1)
        if cls.__name__ == 'Square':
            a = cls(1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """
            loads list of intances from JSON file
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
