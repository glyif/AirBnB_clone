#!/usr/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ test model: amenity """
    def setUp(self):
        """ standard setUp() """
        self.model = Amenity()

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
        self.model.name = "Wifi"
        self.assertEqual(self.model.name, "Wifi")

if __name__ == '__main__':
    unittest.main()
