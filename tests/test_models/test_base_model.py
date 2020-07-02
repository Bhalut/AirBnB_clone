#!/usr/bin/python3
""" test_base_model.py

    Test of base_model
"""

from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os.path as path
import unittest
import pep8
import os


class TestBaseModel(unittest.TestCase):
    """TestBaseModel Class

    Test cases of BaseModel
    """

    def test_base_model_pep8(self):
        """test_base_pep8 test

        Test pep8 for base_model.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_model_init(self):
        """test_base_model_init test

        Test init class
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(dir(my_model), dir(BaseModel()))
        self.assertEqual(type(my_model.id), str)

    def test_base_model_str(self):
        """test_base_model_str test

        Test str of class
        """
        my_model = BaseModel()
        sleep(0.2)
        my_model.name = "Name"
        my_model.save()
        self.assertTrue(type(str(my_model)) is str)
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_base_model_to_dict(self):
        """test_base_model_to_dict test

        Test to_dict method
        """
        my_model = BaseModel()
        self.assertTrue(type(my_model.to_dict()) is dict)

    def test_base_model_instance(self):
        """test_base_model_instance test

        Test Instance class
        """
        model = BaseModel()
        model.name = "Jerry"
        model.year = 27
        self.assertEqual(model.name, "Jerry")
        self.assertEqual(model.year, 27)

    def test_base_model_save(self):
        """test_base_model_save test

        Test save method
        """
        model = BaseModel()
        model.city = "Medellin"
        model.save()
        self.assertTrue(path.exists("file.json"))
        os.remove("file.json")

    def test_base_model_dict(self):
        """test_base_model_dict test

        Test dict class
        """
        my_model = BaseModel()
        my_model.name = "Jerry"
        my_model.number = 89
        self.assertIs(type(my_model.id), str)
        self.assertIs(type(my_model), BaseModel)
        self.assertIs(type(my_model.created_at), datetime)

        my_model_json = my_model.to_dict()
        self.assertIs(type(my_model_json), dict)

        my_new_model = BaseModel(**my_model_json)
        self.assertIs(type(my_new_model.id), str)
        self.assertIs(type(my_new_model), BaseModel)
        self.assertIs(type(my_new_model.created_at), datetime)

        self.assertTrue(my_model is not my_new_model)


if __name__ == '__main__':
    unittest.main()
