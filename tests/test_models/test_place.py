#!/usr/bin/python3
""" test_place.py

    test cases
"""
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
