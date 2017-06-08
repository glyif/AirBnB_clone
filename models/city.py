#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            super().__init__(args[0], kwargs)
        else:
            super().__init__()
        self.state_id = ""
        self.name = ""
