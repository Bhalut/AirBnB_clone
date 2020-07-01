#!/usr/bin/python3
from models.user import User
import os.path as path
import unittest
import pep8


class TestUser(unittest.TestCase):
    def test_user_pep8(self):
        """test_base_pep8 test

        Test pep8 for base_model.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_user_instance(self):
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
        my_user = User()
        my_user.first_name = "Jerry"
        my_user.last_name = "Mouse"
        my_user.email = "jerry@holbertonshool.com"
        my_user.password = "root"
        my_user.save()
        self.assertTrue(path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
