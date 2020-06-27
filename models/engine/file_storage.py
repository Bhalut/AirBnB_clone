#!/usr/bin/python3
"""FileStorage Module"""
import json
import os.path as path


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

    def classes(self, line):
        """Returns True if line is in __objects type, otherwise False"""
        return True if line not in ["BaseModel"] else False

    def create(self):
        """Return dictionary whit classes that can create"""
        from models.base_model import BaseModel

        return {"BaseModel": BaseModel}

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

        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    FileStorage.__objects[key] = BaseModel(**value)
