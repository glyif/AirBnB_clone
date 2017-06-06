#!/usr/bin/python3
from models import storage
import datetime
import uuid

class BaseModel:

    """The base class for all storage objects in this project"""
    def __init__(self, *args, **kwargs):
        """initialize class object"""
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now())

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        self.__dict__["updated_at"] = str(datetime.datetime.now())
        storage.new(self)
        storage.save()


    def to_json(self):
        self.__dict__.update({'__class__': self.__class__.__name__})
        return self.__dict__
