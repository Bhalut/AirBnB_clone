#!/usr/bin/python3
""" test_place.py

    test cases
"""
from models.base_model import BaseModel
from models.place import Place
import os.path as path
import unittest
import pep8


class TestPlace(unittest.TestCase):
    """TestPlace class

    Test cases
    """

    def test_place_pep8(self):
        """test_base_pep8 test

        Test pep8 for place.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_place_attributes(self):
        """test_place_attributes test

        Test instance class
        """
        my_place = Place()
        self.assertTrue(hasattr(my_place, "id"))
        self.assertTrue(hasattr(my_place, "created_at"))
        self.assertTrue(hasattr(my_place, "updated_at"))
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(type(my_place.number_rooms), int)
        self.assertEqual(type(my_place.max_guest), int)

    def test_place_inheritance(self):
        """test_place_inheritance test

        Test instance class
        """
        my_place = Place()
        self.assertIsInstance(my_place, Place)
        self.assertIsInstance(my_place, BaseModel)

    def test_place_amenity(self):
        """test_place_amenity test

        Test instance class
        """
        empty_list = list()
        my_place = Place()
        self.assertEqual(my_place.amenity_ids, empty_list)

    def test_place_price_by_night(self):
        """test_place_price_by_night test

        Test instance class
        """
        my_place = Place()
        my_place.price_by_night = 300
        self.assertEqual(my_place.price_by_night, 300)
        self.assertTrue("price_by_night" in my_place.__dict__)

    def test_place_instance(self):
        """test_place_instance test

        Test instance class
        """
        my_place = Place()
        my_place.first_name = "Jerry"
        my_place.last_name = "Mouse"
        my_place.email = "jerry@holbertonshool.com"
        my_place.password = "root"
        self.assertEqual(my_place.first_name, "Jerry")
        self.assertEqual(my_place.last_name, "Mouse")
        self.assertEqual(my_place.email, "jerry@holbertonshool.com")
        self.assertEqual(my_place.password, "root")

    def test_place_save(self):
        """test_place_save test

        Test save method
        """
        my_place = Place()
        my_place.first_name = "Jerry"
        my_place.last_name = "Mouse"
        my_place.email = "jerry@holbertonshool.com"
        my_place.password = "root"
        my_place.save()
        self.assertTrue(path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
