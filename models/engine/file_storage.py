#!/usr/bin/python3
import json
import datetime

class FileStorage:
    def __init__(self, file_path="./file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        json_obj = {}
        for key in self.__objects.keys():
            json_obj[key] = self.__objects[key].to_json()
        with open(self.__file_path, mode='w') as fd:
            json.dump(json_obj, fd)

    def reload(self):
        try:
            with open(self.__file_path, mode='r') as fd:
                read = fd.read()
                dump = json.loads(read)
                from ..base_model import BaseModel
                for key, value in dump.items():
                    if value.get('__class__') == 'BaseModel':
                        self.__objects[key] = BaseModel(dump[key])
        except FileNotFoundError:
                pass
