#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    base_model that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """init method for BaseModel Class
        Attributes:
            args (list): inputted arguments as a list.
            kwargs (dict): inputted arguments as a dict.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime\
                                       .strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'id':
                    self.id = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str method for BaseModel Class
            Return:
                string (str): string descriptor for BaseModel Class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        Return:
            dictionary (dict): Dictionary object that contains __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
