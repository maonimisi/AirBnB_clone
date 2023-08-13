#!/usr/bin/python3
"""Module for FileStorage class."""
import os
import json
import datetime


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Returns __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets new obj in __objects dictionary
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialzes __objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            data = {k: v.to_dict() for k, v in Filestorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """
        Deserializes JSON file into __objects.
        """
        try:
            with open(f'{type(self).__file_path}', mode='r', encoding='UTF8')\
                 as json_file:
                type(self).__objects = json.load(json_file)
        except FileNotFoundError:
            pass
