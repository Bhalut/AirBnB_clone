#!/usr/bin/python3
""" test_review.py

    test cases
"""
from models.base_model import BaseModel
from models.review import Review
import os.path as path
import unittest
import pep8
import os


class TestReview(unittest.TestCase):
    """TestReview class

    Test cases
    """

    def test_review_pep8(self):
        """test_base_pep8 test

        Test pep8 for review.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_review_attributes(self):
        """test_review_attributes test

        Test instance class
        """
        my_review = Review()
        self.assertTrue(hasattr(my_review, "id"))
        self.assertTrue(hasattr(my_review, "created_at"))
        self.assertTrue(hasattr(my_review, "updated_at"))
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")

    def test_review_inheritance(self):
        """test_review_inheritance test

        Test instance class
        """
        my_review = Review()
        self.assertIsInstance(my_review, Review)
        self.assertIsInstance(my_review, BaseModel)

    def test_review_user(self):
        """test_review_user test

        Test instance class
        """
        my_review = Review()
        my_review.place_id = "0001"
        my_review.user_id = "1234"
        my_review.text = "Nice place"
        self.assertEqual(my_review.place_id, "0001")
        self.assertEqual(my_review.user_id, "1234")
        self.assertEqual(my_review.text, "Nice place")

    def test_review_instance(self):
        """test_review_instance test

        Test instance class
        """
        my_review = Review()
        my_review.first_name = "Jerry"
        my_review.last_name = "Mouse"
        my_review.email = "jerry@holbertonshool.com"
        my_review.password = "root"
        self.assertEqual(my_review.first_name, "Jerry")
        self.assertEqual(my_review.last_name, "Mouse")
        self.assertEqual(my_review.email, "jerry@holbertonshool.com")
        self.assertEqual(my_review.password, "root")

    def test_review_save(self):
        """test_review_save test

        Test save method
        """
        my_review = Review()
        my_review.first_name = "Jerry"
        my_review.last_name = "Mouse"
        my_review.email = "jerry@holbertonshool.com"
        my_review.password = "root"
        my_review.save()
        self.assertTrue(path.exists("file.json"))
        os.remove("file.json")


if __name__ == '__main__':
    unittest.main()
