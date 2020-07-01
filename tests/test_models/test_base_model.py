#!/usr/bin/python3
from models.base_model import BaseModel
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
