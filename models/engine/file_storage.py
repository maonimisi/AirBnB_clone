#!/usr/bin/python3
"""
FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances:
"""
import json


class FileStorage:

    """Class for serializtion and deserialization of base classes"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Returns a dictionary containing all the stored objects
        """
        return type(self).__objects

    def new(self, obj):
        '''
        Add a new object, obj, to __objects, which is the dictionary of
            all stored objects

        Args:
        obj(object): The object to be added to the dictionary of stored objects
        '''
        type(self).__objects[f'{type(obj).__name__}.{obj.id}'] = obj.to_dict()

    def save(self):
        '''
        Serialize the current content of __object into a json file with
        the file path __file_path
        '''
        with open(type(self).__file_path, mode='w', encoding='UTF8') as json_file:
            json.dump(type(self).__objects, json_file)

    def reload(self):
        '''
        Deserialize the content of the json file into the __objects dictionary
        '''
        try:
            with open(f'{type(self).__file_path}', mode='r', encoding='UTF8')\
                 as json_file:
                type(self).__objects = json.load(json_file)
        except FileNotFoundError:
            pass
