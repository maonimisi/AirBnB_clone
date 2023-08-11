#!/usr/bin/env pytihon3
from models.user import User
import unittest
"""
Test the user class
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
        self.user = User()

    def test_class_attr(self):
        """
        Test the class atrriute
        """
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_str_rep(self):
        """
        Test for string representation of user object
        """
        self.assertEqual(self.user.__str__(),
                         "[User] ({}) {}".format(self.user.id,
                                                 self.user.__dict__))

    def test_for_inheritedMethod(self):
        """
        Test for methof inherited from the super class
        """
        user_attr = dir(User)
        self.assertTrue("save" in user_attr)
        self.assertTrue("to_dict" in user_attr)
