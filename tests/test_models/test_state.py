#!/usr/bin/env pytihon3


import unittest
from datetime import datetime
from models.state import State
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def setUp(self):
        """Setup method that runs before each test."""
        self.state = State()

    def tearDown(self):
        """Teardown method that runs after each test."""
        storage.reload()

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test if State attributes are set correctly."""
        self.assertEqual(self.state.name, "")
        self.assertIsNotNone(self.state.id)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)

    def test_created_at_type(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_save_method(self):
        """Test if save method updates the updated_at attribute."""
        old_updated_at = self.state.updated_at
        self.state.save()
        new_updated_at = self.state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary representation."""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_from_dict_method(self):
        """Test if from_dict method recreates an instance from a dictionary."""
        state_dict = self.state.to_dict()
        new_instance = State(**state_dict)
        self.assertIsInstance(new_instance, State)
        self.assertEqual(self.state.id, new_instance.id)
        self.assertEqual(self.state.created_at, new_instance.created_at)
        self.assertEqual(self.state.updated_at, new_instance.updated_at)
        self.assertEqual(self.state.name, new_instance.name)


if __name__ == '__main__':
    unittest.main()
