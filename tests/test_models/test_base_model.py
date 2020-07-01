#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
import os.path as path
import unittest
import pep8


class TestBaseModel(unittest.TestCase):
    def test_base_model_pep8(self):
        """test_base_pep8 test

        Test pep8 for base_model.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_model_instance(self):
        model = BaseModel()
        model.name = "Jerry"
        model.year = 27
        self.assertEqual(model.name, "Jerry")
        self.assertEqual(model.year, 27)

    def test_base_model_save(self):
        model = BaseModel()
        model.city = "Medellin"
        model.save()
        self.assertTrue(path.exists("file.json"))

    def test_base_model_dict(self):
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
