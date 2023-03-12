#!/usr/bin/python3
"""This is the file storage module"""
import json
import os


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes object to json file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """"deserializes json filebto object"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
