#!/usr/bin/python3
"""Base class for all models of hbnb clone"""

import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of base instance
        args:
            - *args: list of arguments (not used in this implementation)
            - **kwargs: dictionary of key, value pairs
        """
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs.keys()) > 0:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, fmt)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, fmt)
                else:
                    exec(f'self.{key} = value')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = str(self.created_at.isoformat())
        my_dict["updated_at"] = str(self.updated_at.isoformat())
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """String representation for BaseModel instance"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'
