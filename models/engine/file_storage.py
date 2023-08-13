#!/usr/bin/python3
"""
FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances:
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    """FileStorage class for serializtion and deserialization of objects
    into and from files
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        init method for FileStorage class
        """
        pass

    def all(self):
        """
        Returns a dictionary containing all the stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object, obj, to __objects, which is the dictionary of
        all stored objects

        Args:
        obj(object): The object to be added to the dictionary of stored objects
        """
        my_dict = obj.to_dict()
        key = "{}.{}".format(dictionary["__class__"], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serialize the current content of __object into a json file with
        the file path __file_path
        '''
        dictionary = dict()
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        '''
        Deserialize the content of the json file into the __objects dictionary
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except:
            pass
