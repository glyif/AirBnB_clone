#!/usr/bin/python3
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """ test model: state """
    def setUp(self):
        """ standard setUp() """
        self.model = State()

    def test_public_attr(self):
        """
        check if public attribute exists and if equal to empty string-
        name("")
        """
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")

    def test_string(self):
        """
        assertEqual input for each attr
        """
        self.model.name = "California"
        self.assertEqual(self.model.name, "California")

if __name__ == '__main__':
    unittest.main()
