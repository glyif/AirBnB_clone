#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.state_id = ""
        name = ""
