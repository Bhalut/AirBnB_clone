#!/usr/bin/python3
""" test_amenity.py

    test cases
"""
from models.base_model import BaseModel
from models.amenity import Amenity
import os.path as path
import unittest
import pep8


class TestAmenity(unittest.TestCase):
    """TestAmenity class

    test cases
    """

    def test_amenity_pep8(self):
        """test_base_pep8 test

        Test pep8 for amenity.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_amenity_attributes(self):
        """test_amenity_attributes test

        Test instance class
        """
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, "id"))
        self.assertTrue(hasattr(my_amenity, "created_at"))
        self.assertTrue(hasattr(my_amenity, "updated_at"))
        self.assertEqual(my_amenity.name, "")

    def test_amenity_inheritance(self):
        """test_amenity_inheritance test

        Test instance class
        """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
        self.assertIsInstance(my_amenity, BaseModel)

    def test_amenity_instance(self):
        """test_amenity_instance test

        Test instance class
        """
        my_amenity = Amenity()
        my_amenity.first_name = "Jerry"
        my_amenity.last_name = "Mouse"
        my_amenity.email = "jerry@holbertonshool.com"
        my_amenity.password = "root"
        self.assertEqual(my_amenity.first_name, "Jerry")
        self.assertEqual(my_amenity.last_name, "Mouse")
        self.assertEqual(my_amenity.email, "jerry@holbertonshool.com")
        self.assertEqual(my_amenity.password, "root")

    def test_amenity_save(self):
        """test_amenity_save test

        Test instance class
        """
        my_amenity = Amenity()
        my_amenity.first_name = "Jerry"
        my_amenity.last_name = "Mouse"
        my_amenity.email = "jerry@holbertonshool.com"
        my_amenity.password = "root"
        my_amenity.save()
        self.assertTrue(path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
