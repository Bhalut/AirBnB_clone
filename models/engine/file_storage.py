#!/usr/bin/python3
"""FileStorage Module"""
import json
import os.path as path
import datetime


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
        return FileStorage.__objects

    def dictionary(self):
        """Return dictionary whit classes that can create"""
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        return {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User}

    def destroy(self, line):
        """Destroy a specific object in __objects"""
        del FileStorage.__objects[line]
        self.save()

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = {key: value.to_dict()
                for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User

        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    keys = key.split(".")
                    if keys[0] in self.dictionary():
                        FileStorage.__objects[key] = self.dictionary()[
                            keys[0]](**value)
