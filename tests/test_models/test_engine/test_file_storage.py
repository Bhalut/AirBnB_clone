#!/usr/bin/python3
""" test_file_storage.py

    Test of file_storage
"""
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime
from time import sleep
import os.path as path
import unittest
import pep8
import os


class TestFileStorage(unittest.TestCase):
    """TestFileStorage Class

    Test cases of FileStorage
    """

    def test_file_storage_pep8(self):
        """test_file_storage test

        Test pep8 for file_storage.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_file_storage_dictionary(self):
        """test_file_storage_dictionary test

        Test class
        """
        dictionary = {'BaseModel': BaseModel,
                      'User': User,
                      'State': State,
                      'City': City,
                      'Amenity': Amenity,
                      'Place': Place,
                      'Review': Review}
        self.assertEqual(storage.dictionary(), dictionary)
        self.assertEqual(storage.dictionary(), FileStorage.dictionary(storage))

    def test_file_storage_new_amenity(self):
        """test_file_storage_amenity test

        Test class
        """
        my_amt = Amenity()
        storage.new(my_amt)
        self.assertTrue(storage.all()[type(my_amt).__name__ + "." + my_amt.id])

    def test_file_storage_new_base_model(self):
        """test_file_storage_base_model test

        Test class
        """
        my_bs = BaseModel()
        storage.new(my_bs)
        self.assertTrue(
            storage.all()[type(my_bs).__name__ + "." + my_bs.id])

    def test_file_storage_new_city(self):
        """test_file_storage_city test

        Test class
        """
        my_city = City()
        storage.new(my_city)
        self.assertTrue(
            storage.all()[type(my_city).__name__ + "." + my_city.id])

    def test_file_storage_new_place(self):
        """test_file_storage_place test

        Test class
        """
        my_place = Place()
        storage.new(my_place)
        self.assertTrue(
            storage.all()[type(my_place).__name__ + "." + my_place.id])

    def test_file_storage_new_review(self):
        """test_file_storage_review test

        Test class
        """
        my_rvw = Review()
        storage.new(my_rvw)
        self.assertTrue(storage.all()[type(my_rvw).__name__ + "." + my_rvw.id])

    def test_file_storage_new_state(self):
        """test_file_storage_state test

        Test class
        """
        my_stt = State()
        storage.new(my_stt)
        self.assertTrue(storage.all()[type(my_stt).__name__ + "." + my_stt.id])

    def test_file_storage_new_user(self):
        """test_file_storage_user test

        Test class
        """
        my_usr = User()
        storage.new(my_usr)
        self.assertTrue(storage.all()[type(my_usr).__name__ + "." + my_usr.id])

    def test_file_storage_reload(self):
        """ test if 'reload' reads 'file.json' and fill __objects """
        my_user = User()
        storage.new(my_user)
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        key = type(my_user).__name__ + "." + my_user.id
        self.assertTrue(key in FileStorage._FileStorage__objects)
        os.remove("file.json")


if __name__ == "__main__":
    unittest.main()
