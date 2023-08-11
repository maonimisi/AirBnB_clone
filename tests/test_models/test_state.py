#!/usr/bin/env pytihon3
from models.state import State
import unittest
"""
Unit test cases for the the user class
"""


class TestUserClass(unittest.TestCase):
    """
    Test for user class models in the file
    storage engine
    """

    def setUp(self):
        """
        setup the user class instance for the test cases
        """
        self.state = State()

    def test_class_attr(self):
        """
        Test the class atrriute
        """
        self.assertTrue(hasattr(State, "name"))

    def test_str_rep(self):
        """
        Test for string representation of user object
        """
        self.assertEqual(self.state.__str__(),
                         "[State] ({}) {}".format(self.state.id,
                                                  self.state.__dict__))

    def test_for_inheritedMethod(self):
        """
        Test for method inherited from the super class
        """
        state_attr = dir(State)
        self.assertTrue("save" in state_attr)
        self.assertTrue("to_dict" in state_attr)
