#!/usr/bin/python3
""" test_city.py

    test cases
"""
from models.city import City
import os.path as path
import unittest
import pep8


class TestCity(unittest.TestCase):
    """TestCity class

    test cases
    """

    def test_city_pep8(self):
        """test_base_pep8 test

        Test pep8 for city.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_city_instance(self):
        """test_city_instance test

        Test instance class
        """
        my_city = City()
        my_city.first_name = "Jerry"
        my_city.last_name = "Mouse"
        my_city.email = "jerry@holbertonshool.com"
        my_city.password = "root"
        self.assertEqual(my_city.first_name, "Jerry")
        self.assertEqual(my_city.last_name, "Mouse")
        self.assertEqual(my_city.email, "jerry@holbertonshool.com")
        self.assertEqual(my_city.password, "root")

    def test_city_save(self):
        """test_city_save test

        Test save method
        """
        my_city = City()
        my_city.first_name = "Jerry"
        my_city.last_name = "Mouse"
        my_city.email = "jerry@holbertonshool.com"
        my_city.password = "root"
        my_city.save()
        self.assertTrue(path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
