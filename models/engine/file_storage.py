#!/usr/bin/python3
import json
import datetime

class DateDecoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return (obj.isoformat())
        return (obj.__dict)

class FileStorage:
    def __init__(self):
        self.__file_path = "./file.json"
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
            json.dump(json_obj, fd, cls=DateDecoder)

    def reload(self):
        try:
            with open(self.__file_path, mode='r') as fd:
                read = fd.read()
                dump = json.loads(read)
                from ..base_model import BaseModel
                for key, value in dump.items():
                    if value.get('__class__') == 'BaseModel':
                        self.__objects[key] = BaseModel(dump[key])
                    if value.get('__class__') == 'User':
                        self.__objects[key] = User(dump[key])
        except FileNotFoundError:
                pass
