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
