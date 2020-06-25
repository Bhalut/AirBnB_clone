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
        """Instance Initializer"""
        self.id = str(uuid4())
        self.created_ad = datetime.now()
        self.update_ad = datetime.now()

    def __str__(self):
        msg = "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)
        return msg

    def save(self):
        """Save last time instance modification"""
        self.update_ad = datetime.today()

    def to_dict(self):
        dictionary = self.__dict__
        return dictionary

# if __name__ == "__main__":
#     a = BaseModel()
#     print(a.id)
#     print(a.update_ad)

#     time.sleep(2)
#     a.id = "45"
#     a.save()
    # print(a.update_ad)
