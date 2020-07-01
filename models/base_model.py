#!/usr/bin/python3
"""Module BaseModule"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel Class
    Public instance attributes:
        id: Type string (unique id)
        created_ad: Creation date
        update_ad: Last modification date
    Public instance methods:
        def save(): save last time object modification
        def to_dict(): returns a dictionary containing all instances
    """

    def all(self):
        """Print all objects"""
        print(self.__str__)

    def __init__(self, *args, **kwargs):
        """Initialize Object"""
        data = [__class__, "created_at", "updated_at",
                "id", "name", "my_number"]
        for key, value in kwargs.items():
            if key in data:
                if key == "created_at" or key == "updated_at":
                    dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dt)
                else:
                    setattr(self, key, value)

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns object representation (human readeable)"""
        m = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return m

    def save(self):
        """Save last time instance modification"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary
