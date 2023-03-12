#!/usr/bin/python3
"""This is the file storage module"""
import json
import os
from importlib import import_module


class FileStorage():
    """This is the file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects fict"""
        return FileStorage.__objects

    def new(self, obj):
        """sets _objects with key value"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes object to json file"""
        objcopy = {}
        for key in FileStorage.__objects.keys():
            obj = FileStorage.__objects[key]
            objcopy[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objcopy, f)

    def reload(self):
        """"deserializes json filebto object"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                objects = json.load(f)
            clsmod = {'BaseModel': "models.base_model"}
            for key, value in objects.items():
                clsnm = value["__class__"]
                for k, v in clsmod.items():
                    if clsnm == k:
                        mymod = import_module(v)
                        break
                mycls = getattr(mymod, clsnm)
                FileStorage.__objects[key] = mycls(**value)
