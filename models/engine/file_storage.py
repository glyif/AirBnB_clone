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
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

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
                from models.base_model import BaseModel
                from models.amenity import Amenity
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User
                class_list = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]
                for key, value in dump.items():
                    if value.get('__class__') in class_list:
                        function = value.get('__class__')
                        self.__objects[key] = eval(str(function))(dump[key])
        except FileNotFoundError:
                pass
