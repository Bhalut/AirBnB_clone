#!/usr/bin/python3
"""Review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class
    Public class attributes:
        name: type string
        user_id: type string
        text: type string
    """
    place_id = ""
    user_id = ""
    text = ""
