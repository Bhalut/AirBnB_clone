#!/usr/bin/python3
""" test_state.py

    test cases
"""
from models.base_model import BaseModel
from models.state import State
import os.path as path
import unittest
import pep8


class TestState(unittest.TestCase):
    """TestState class

    Test cases
    """

    def test_state_pep8(self):
        """test_base_pep8 test

        Test pep8 for state.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_state_attributes(self):
        """test_state_attributes test

        Test instance class
        """
        my_state = State()
        self.assertTrue(hasattr(my_state, "id"))
        self.assertTrue(hasattr(my_state, "created_at"))
        self.assertTrue(hasattr(my_state, "updated_at"))
        self.assertEqual(my_state.name, "")

    def test_state_inheritance(self):
        """test_state_inheritance test

        Test instance class
        """
        my_state = State()
        self.assertIsInstance(my_state, State)
        self.assertIsInstance(my_state, BaseModel)

    def test_state_name(self):
        """test_state_name test

        Test instance class
        """
        my_state = State()
        my_state.name = "Cartagena"
        self.assertEqual(my_state.name, "Cartagena")

    def test_state_instance(self):
        """test_State_instance test

        Test instance class
        """
        my_state = State()
        my_state.first_name = "Jerry"
        my_state.last_name = "Mouse"
        my_state.email = "jerry@holbertonshool.com"
        my_state.password = "root"
        self.assertEqual(my_state.first_name, "Jerry")
        self.assertEqual(my_state.last_name, "Mouse")
        self.assertEqual(my_state.email, "jerry@holbertonshool.com")
        self.assertEqual(my_state.password, "root")

    def test_state_save(self):
        """test_state_save test

        Test save method
        """
        my_state = State()
        my_state.first_name = "Jerry"
        my_state.last_name = "Mouse"
        my_state.email = "jerry@holbertonshool.com"
        my_state.password = "root"
        my_state.save()
        self.assertTrue(path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
