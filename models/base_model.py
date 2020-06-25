#!/usr/bin/python3
"""Module BaseModule
"""
from uuid import uuid4
from datetime import datetime
import time


class BaseModel:
    """BaseModel Class
    Public instance attributes:
        id = Type string (unique id)
        created_ad = Creation date
        update_ad = Last modification date
    Public instance methods:
    """

    def __init__(self):
        """Initialize Object"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns object representation (human readeable)"""
        msg = "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)
        return msg

    def save(self):
        """Save last time instance modification"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = BaseModel.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary

