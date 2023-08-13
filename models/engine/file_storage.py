#!/usr/bin/python3
"""
FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances:
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class for serialization and deserialization of objects
    into and from files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all the stored objects
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object, obj, to __objects, the dictionary of
        all stored objects

        Args:
            obj (BaseModel): The object to be added to the dictionary of
            stored objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the current content of __objects into a JSON file
        """
        my_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(my_dict, file)

    def reload(self):
        """
        Deserialize the content of the JSON file into the __objects dictionary
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for key, value in json_load.items():
                class_name = value["__class__"]
                del value["__class__"]
                self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass
