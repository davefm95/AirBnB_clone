#!/usr/bin/python3
"""This is the base model module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Thid thr base model class"""
    def __init__(self, *args, **kwargs):
        """This initializes the instance"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    form = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, form)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """The str representation of the class"""
        return f"[{self.__class__.__name__}] [{self.id}] {self.__dict__}"

    def save(self):
        """uodates self.updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dict containing all instance attributes"""
        dct = {}
        dct.update(self.__dict__)
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.isoformat()
        dct["updated_at"] = self.updated_at.isoformat()
        return dct
