#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ test engine: file storage """
    def setUp(self):
        """ standard setUp() """
        self.file_storage = FileStorage()

    def test_public_attr(self):
        """ test if attributes exist """
        self.assertFalse(hasattr(self.file_storage, "foo.json"))

""" def test_all(self):

    def test_new(self):

    def test_save(self):

    def test_reload(self): """

if "__main__" == __name__:
    unittest.main()
