#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            super().__init__(args[0], kwargs)
        else:
            super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
