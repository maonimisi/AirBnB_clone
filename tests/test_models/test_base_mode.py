#!/usr/bin/python3


import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Setup method that runs before each test."""
        self.base_model = BaseModel()

    def tearDown(self):
        """Teardown method that runs after each test."""
        storage.reset()

    def test_attributes(self):
        """Test if BaseModel attributes are set correctly."""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_created_at_type(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        """Test if save method updates the updated_at attribute."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary representation."""
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_from_dict_method(self):
        """Test if from_dict method recreates an instance from a dictionary."""
        model_dict = self.base_model.to_dict()
        new_instance = BaseModel(**model_dict)
        self.assertIsInstance(new_instance, BaseModel)
        self.assertEqual(self.base_model.id, new_instance.id)
        self.assertEqual(self.base_model.created_at, new_instance.created_at)
        self.assertEqual(self.base_model.updated_at, new_instance.updated_at)


if __name__ == '__main__':
    unittest.main()
