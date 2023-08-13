#!/usr/bin/env pytihon3


import unittest
from datetime import datetime
from models.user import User
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        """Setup method that runs before each test."""
        self.user = User()

    def tearDown(self):
        """Teardown method that runs after each test."""
        storage.reload()

    def test_inheritance(self):
        """Test if User inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test if User attributes are set correctly."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

    def test_created_at_type(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_save_method(self):
        """Test if save method updates the updated_at attribute."""
        old_updated_at = self.user.updated_at
        self.user.save()
        new_updated_at = self.user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary representation."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_from_dict_method(self):
        """Test if from_dict method recreates an instance from a dictionary."""
        user_dict = self.user.to_dict()
        new_instance = User(**user_dict)
        self.assertIsInstance(new_instance, User)
        self.assertEqual(self.user.id, new_instance.id)
        self.assertEqual(self.user.created_at, new_instance.created_at)
        self.assertEqual(self.user.updated_at, new_instance.updated_at)
        self.assertEqual(self.user.email, new_instance.email)
        self.assertEqual(self.user.password, new_instance.password)
        self.assertEqual(self.user.first_name, new_instance.first_name)
        self.assertEqual(self.user.last_name, new_instance.last_name)

if __name__ == '__main__':
    unittest.main()

