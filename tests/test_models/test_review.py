#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ test model: review """
    def setUp(self):
        """ standard setUp() """
        self.model = Review()

    def test_public_attr(self):
        """
        check if public attribute exists and if equal to empty string-
        state_id("", State.id), name("")
        """
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")

    def test_strings(self):
        """
        assertEqual input for each attr
        """
        self.model.place_id = 42
        self.model.user_id = 98
        self.model.text = "foo"
        self.assertEqual(self.model.place_id, 42)
        self.assertEqual(self.model.user_id, 98)
        self.assertEqual(self.model.text, "foo")

if __name__ == '__main__':
    unittest.main()
