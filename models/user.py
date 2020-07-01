#!/usr/bin/python3
"""User Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class
    Public class attributes:
        email: type string
        password: type string
        first_name: type string
        last_name: type string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
