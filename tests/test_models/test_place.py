#!/usr/bin/python3
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """ test model: place """
    def setUp(self):
        """ standard setUp() """
        self.model = Place()
        self.model.save()

    def test_public_attr(self):
        """
        check if public attribute exists and if equal to empty string, int, or
        float- city_id(""), user_id(""), name(""), description(""),
        number_rooms(0), number_bathrooms(0), max_guest(0), price_by_night(0),
        latitude(0.0), longitude(0.0), amenities([''])
        """
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenities"))
        self.asserEqual(self.model.city_id, "")
        self.asserEqual(self.model.user_id, "")
        self.asserEqual(self.model.name, "")
        self.asserEqual(self.model.description, "")
        self.asserEqual(self.model.number_rooms, 0)
        self.asserEqual(self.model.number_bathrooms, 0)
        self.asserEqual(self.model.max_guest, 0)
        self.asserEqual(self.model.price_by_night, 0)
        self.asserEqual(self.model.latitude, 0.0)
        self.asserEqual(self.model.longitude, 0.0)
        self.asserEqual(self.model.amenity_ids, [''])

    def test_string_int_float(self):
        """
        assertEqual input for each attr
        """
        self.model.city_id = 42
        self.model.user_id = 98
        self.model.name = "Betty"
        self.model.description = "hello, world"
        self.model.number_rooms = 2
        self.model.number_bathrooms = 1
        self.model.max_guest = 3
        self.model.price_by_night = 200
        self.model.latitude = 1.1
        self.model.longitude = 1.2
        self.model.amenity_ids = ['1234', '12345']
        self.assertEqual(self.model.city_id, 42)
        self.assertEqual(self.model.user_id, 98)
        self.assertEqual(self.model.name, "Betty")
        self.assertEqual(self.model.description, "hello, world")
        self.assertEqual(self.model.number_rooms, 2)
        self.assertEqual(self.model.number_bathrooms, 1)
        self.assertEqual(self.model.max_guest, 3)
        self.assertEqual(self.model.price_by_night, 200)
        self.assertEqual(self.model.latitude, 1.1)
        self.assertEqual(self.model.longitude, 1.2)
        self.assertEqual(self.model.amenity_ids, ['1234', '12345'])

if __name__ == '__main__':
    unittest.main()
