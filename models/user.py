#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
import uuid


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
