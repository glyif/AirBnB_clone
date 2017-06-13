#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ test model: city """
    def setUp(self):
        """ standard setUp() """
        self.model = City()

    def test_public_attr(self):
        """
        check if public attribute exists and if equal to empty string-
        state_id("", State.id), name("")
        """
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.state_id, "")
        self.assertEqual(self.model.name, "")

    def test_strings(self):
        """
        assertEqual input for each attr
        """
        self.model.name = "San Francisco"
        self.model.state_id = "7d78d8de-a37f-4edd-9443-1578032a1eea"
        self.assertEqual(self.model.name, "San Francisco")
        self.assertEqual(self.model.state_id,
                         "7d78d8de-a37f-4edd-9443-1578032a1eea")

if __name__ == '__main__':
    unittest.main()
