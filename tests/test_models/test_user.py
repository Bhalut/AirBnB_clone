#!/usr/bin/python3
""" test_user.py

    test cases
"""
from models.base_model import BaseModel
from models.user import User
import os.path as path
import unittest
import pep8


class TestUser(unittest.TestCase):
    """TestUser class

    Test cases
    """

    def test_user_pep8(self):
        """test_base_pep8 test

        Test pep8 for user.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_user_attributes(self):
        """test_user_attributes test

        Test instance class
        """
        my_user = User()
        self.assertTrue(hasattr(my_user, "id"))
        self.assertTrue(hasattr(my_user, "created_at"))
        self.assertTrue(hasattr(my_user, "updated_at"))
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")

    def test_user_inheritance(self):
        """test_user_inheritance test

        Test instance class
        """
        my_user = User()
        self.assertIsInstance(my_user, User)
        self.assertIsInstance(my_user, BaseModel)

    def test_user_instance(self):
        """test_user_instance test

        Test instance class
        """
        my_user = User()
        my_user.first_name = "Jerry"
        my_user.last_name = "Mouse"
        my_user.email = "jerry@holbertonshool.com"
        my_user.password = "root"
        self.assertEqual(my_user.first_name, "Jerry")
        self.assertEqual(my_user.last_name, "Mouse")
        self.assertEqual(my_user.email, "jerry@holbertonshool.com")
        self.assertEqual(my_user.password, "root")

    def test_user_save(self):
        """test_user_save test

        Test save method
        """
        my_user = User()
        my_user.first_name = "Jerry"
        my_user.last_name = "Mouse"
        my_user.email = "jerry@holbertonshool.com"
        my_user.password = "root"
        my_user.save()
        self.assertTrue(path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
