#!/usr/bin/python3
"""The reviews Module"""
from models.base_model import BaseModel


class Reviews(BaseModel):
    """reviews class inherits basemodel"""
    place_id = ""
    user_id = ""
    text = ""
