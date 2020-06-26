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
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = self.__to_json_string(
            [obj.to_dictionary() for obj in FileStorage.__objects])
        filename = FileStorage.__file_path
        with open(filename, 'a') as file:
            file.write(data)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        pass

    def __to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Parameters: list_dictionaries
        """
        return json.dumps(list_dictionaries)

    def __from_json_string(self, json_string):
        """Returns the list of the JSON string representation
        Parameters:
            json_string: string info JSON format
        Raises:
            TypeError: json_string must be a string
        """
        if json_string in [None, ""]:
            return []
        elif type(json_string) != str:
            raise TypeError("json_string must be a string")
        else:
            return json.loads(json_string)
