#!/usr/bin/python
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test model: user"""
    def setUp(self):
        """ standard setUp()"""
        self.model = User()

    def test_oublic_attr(self):
        """
        check if public attributes are exist and if equal to empty string-
        email(""), password(""), first_name(""), last_name("")
        """
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")

    def test_strings(self):
        """
        assertEqual input for each attr
        """
        self.model.email = "airbnb@holbertonshool.com"
        self.model.password = "root"
        self.model.first_name = "Betty"
        self.model.last_name = "Holberton"
        self.assertEqual(self.model.email, "airbnb@holbertonshool.com")
        self.assertEqual(self.model.password, "root")
        self.assertEqual(self.model.first_name, "Betty")
        self.assertEqual(self.model.last_name, "Holberton")

if __name__ == '__main__':
    unittest.main()
