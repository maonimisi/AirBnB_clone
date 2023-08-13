#!/usr/bin/env pytihon3


import unittest
from datetime import datetime
from models.review import Review
from models import storage
from models.base_model import BaseModel

class TestReview(unittest.TestCase):

    def setUp(self):
        """Setup method that runs before each test."""
        self.review = Review()

    def tearDown(self):
        """Teardown method that runs after each test."""
        storage.reload()

    def test_inheritance(self):
        """Test if Review inherits from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test if Review attributes are set correctly."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertIsNotNone(self.review.id)
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)

    def test_created_at_type(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_save_method(self):
        """Test if save method updates the updated_at attribute."""
        old_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary representation."""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_from_dict_method(self):
        """Test if from_dict method recreates an instance from a dictionary."""
        review_dict = self.review.to_dict()
        new_instance = Review(**review_dict)
        self.assertIsInstance(new_instance, Review)
        self.assertEqual(self.review.id, new_instance.id)
        self.assertEqual(self.review.created_at, new_instance.created_at)
        self.assertEqual(self.review.updated_at, new_instance.updated_at)
        self.assertEqual(self.review.place_id, new_instance.place_id)
        self.assertEqual(self.review.user_id, new_instance.user_id)
        self.assertEqual(self.review.text, new_instance.text)

if __name__ == '__main__':
    unittest.main()

