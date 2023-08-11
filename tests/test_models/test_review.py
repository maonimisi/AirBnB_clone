#!/usr/bin/env pytihon3
from models.review import Review
import unittest
"""
Unit test case for the user class
"""


class TestUserClass(unittest.TestCase):
    """
    Test for user class models in the dtabase file
    storage engine
    """

    def setUp(self):
        """
        setup the user class instance for test cases
        """
        self.review = Review()

    def test_class_attr(self):
        """
        Test the class atrriute
        """
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_str_rep(self):
        """
        Test for string representation of user object
        """
        self.assertEqual(self.review.__str__(),
                         "[Review] ({}) {}".format(self.review.id,
                                                   self.review.__dict__))

    def test_for_inheritedMethod(self):
        """
        Test for method inherited from the super class
        """
        review_attr = dir(Review)
        self.assertTrue("save" in review_attr)
        self.assertTrue("to_dict" in review_attr)
