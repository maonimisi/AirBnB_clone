#!/usr/bin/python3


import unittest
from datetime import datetime
from models.city import City
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        """Setup method that runs before each test."""
        self.city = City()

    def tearDown(self):
        """Teardown method that runs after each test."""
        storage.reload()

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test if City attributes are set correctly."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        self.assertIsNotNone(self.city.id)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)

    def test_created_at_type(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_save_method(self):
        """Test if save method updates the updated_at attribute."""
        old_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary representation."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_from_dict_method(self):
        """Test if from_dict method recreates an instance from a dictionary."""
        city_dict = self.city.to_dict()
        new_instance = City(**city_dict)
        self.assertIsInstance(new_instance, City)
        self.assertEqual(self.city.id, new_instance.id)
        self.assertEqual(self.city.created_at, new_instance.created_at)
        self.assertEqual(self.city.updated_at, new_instance.updated_at)
        self.assertEqual(self.city.state_id, new_instance.state_id)
        self.assertEqual(self.city.name, new_instance.name)

if __name__ == '__main__':
    unittest.main()
