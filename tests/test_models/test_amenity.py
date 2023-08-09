#!/usr/bin/python3


import unittest
from datetime import datetime
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Setup method that runs before each test."""
        self.amenity = Amenity()

    def tearDown(self):
        """Teardown method that runs after each test."""
        storage.reset()

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test if Amenity attributes are set correctly."""
        self.assertEqual(self.amenity.name, "")
        self.assertIsNotNone(self.amenity.id)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)

    def test_created_at_type(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_save_method(self):
        """Test if save method updates the updated_at attribute."""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        new_updated_at = self.amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary representation."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_from_dict_method(self):
        """Test if from_dict method recreates an instance from a dictionary."""
        amenity_dict = self.amenity.to_dict()
        new_instance = Amenity(**amenity_dict)
        self.assertIsInstance(new_instance, Amenity)
        self.assertEqual(self.amenity.id, new_instance.id)
        self.assertEqual(self.amenity.created_at, new_instance.created_at)
        self.assertEqual(self.amenity.updated_at, new_instance.updated_at)
        self.assertEqual(self.amenity.name, new_instance.name)


if __name__ == '__main__':
    unittest.main()
