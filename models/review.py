#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        if len(args) < 0:
            super().__init__(args[0], kwargs)
        else:
            super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
