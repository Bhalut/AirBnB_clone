#!/usr/bin/python3
"""FileStorage Module
"""
import json


class FileStorage:
    """FileStorage Class
    Private class attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - will store all objects by <class name>.id
    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file
        reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return __objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        pass

    def save(self):
        """serializes __objects to the JSON file"""
        pass

    def reload(self):
        """Deserializes the JSON file to __objects"""
        pass
