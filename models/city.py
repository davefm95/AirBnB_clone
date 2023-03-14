#!/usr/bin/python3
"""Tye city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inheruts from basemodel"""
    state_id = ""
    name = ""
