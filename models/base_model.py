#!/usr/bin/env python3
"""This is the base model module"""
import uuid
import datetime


class BaseModel:
    """Thid thr base model class"""
    def __init__(self):
        """This initializes the instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """The str representation of the class"""
        return f"[{self.__class__.__name__}] [{self.id}] {self.__dict__}"

    def save(self):
        """uodates self.updated_at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns dict containing all instance attributes"""
        dct = self.__dict__
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.isoformat()
        dct["updated_at"] = self.updated_at.isoformat()
        return dct
