#!/usr/bin/python3
"""The user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from base model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
