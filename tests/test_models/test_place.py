#!/usr/bin/python3


import unittest
from datetime import datetime
from models.place import Place
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Setup method that runs before each test."""
        self.place = Place()

    def tearDown(self):
        """Teardown method that runs after each test."""
        storage.reload()

    def test_inheritance(self):
        """Test if Place inherits from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test if Place attributes are set correctly."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsNotNone(self.place.id)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)

    def test_created_at_type(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_save_method(self):
        """Test if save method updates the updated_at attribute."""
        old_updated_at = self.place.updated_at
        self.place.save()
        new_updated_at = self.place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary representation."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_from_dict_method(self):
        """Test if from_dict method recreates an instance from a dictionary."""
        place_dict = self.place.to_dict()
        new_instance = Place(**place_dict)
        self.assertIsInstance(new_instance, Place)
        self.assertEqual(self.place.id, new_instance.id)
        self.assertEqual(self.place.created_at, new_instance.created_at)
        self.assertEqual(self.place.updated_at, new_instance.updated_at)
        self.assertEqual(self.place.city_id, new_instance.city_id)
        self.assertEqual(self.place.user_id, new_instance.user_id)
        self.assertEqual(self.place.name, new_instance.name)
        self.assertEqual(self.place.description, new_instance.description)
        self.assertEqual(self.place.number_rooms, new_instance.number_rooms)
        self.assertEqual(self.place.max_guest, new_instance.max_guest)
        self.assertEqual(self.place.latitude, new_instance.latitude)
        self.assertEqual(self.place.longitude, new_instance.longitude)
        self.assertEqual(self.place.amenity_ids, new_instance.amenity_ids)


if __name__ == '__main__':
    unittest.main()
